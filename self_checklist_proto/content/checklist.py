from ..models import *
from ..language import translator
from django.db.models import Count

def _counter():
  count = [0]
  def func():
    count[0] += 1
    return count[0]
  return func
counter = _counter()

class Checklist:
  def __init__(self, title_key, progression, sections):
    self.title_key = title_key
    self.progression = progression
    self.sections = sections

  def populate(self, user):
    return Checklist(
      self.title_key,
      self.progression.populate(user),
      [s.populate(user, self) for s in self.sections]
    )
  
  def find_option_key(self, option_name):
    for section in self.sections:
      key = section.find_option_key(option_name)
      if key:
        return key


class Progression:
  def __init__(self, top_image_name, steps):
    self.top_image_name = top_image_name
    self.steps = steps

  def populate(self, user):
    return Progression(self.top_image_name, [s.populate(user) for s in self.steps])

  
class ProgressionStep:
  def __init__(self, title_key, image_name, finished_image_name, linked_section, finished=False):
    self.title_key = title_key
    self.image_name = image_name
    self.finished_image_name = finished_image_name
    self.linked_section = linked_section
    self.finished = finished

  def populate(self, user):
    return ProgressionStep(self.title_key, self.image_name, self.finished_image_name, self.linked_section, self.finished)


class Section:
  def __init__(self, section_name, title_key, items):
    self.section_name = section_name
    self.title_key = title_key
    self.items = items

  def populate(self, user, checklist):
    return Section(self.section_name, self.title_key, [i.populate(user) for i in self.items])
  
  def find_option_key(self, option_name):
    for item in self.items:
      key = item.find_option_key(option_name)
      if key:
        return key


class Item:
  def __init__(self, title_key, content, id=None):
    self.id = id if id is not None else counter()
    self.title_key = title_key
    self.content = content

  def populate(self, user):
    return Item(self.title_key, self.content.populate(user), self.id)
  
  def find_option_key(self, option_name):
    if isinstance(self.content, ContentSurvey):
      return self.content.find_option_key(option_name)
    elif isinstance(self.content, ContentList):
      if self.content.list_name == option_name:
        return self.title_key
    return None
  
class Content:
  def __init__(self, content_type) -> None:
    self.content_type = content_type

  def populate(self, user):
    return self

class ContentBody(Content):
  def __init__(self, body_key):
    super().__init__("body")
    self.body_key = body_key

class ContentList(Content):
  def __init__(self, list_name, entries):
    super().__init__("list")
    self.list_name = list_name
    self.entries = entries
  
class ContentListEntry:
  def __init__(self, body_key):
    self.body_key = body_key

class ContentSurvey(Content):
  def __init__(self, survey_name, options, followups=[], completed=False, subtitle=None, hide_graph=False):
    super().__init__("survey")
    self.survey_name = survey_name
    self.options = options
    self.followups = followups
    self.completed = completed
    self.subtitle = subtitle
    self.hide_graph = hide_graph

  def get_data(self, lang):
    return {
      "labels": [translator.t(o.option_key, lang=lang) for o in self.options],
      "datasets": [{
        "data": [o.total for o in self.options],
        "backgroundColor": [o.colour for o in self.options],
        "hoverOffset": 4
      }]
    }

  def populate(self, user):
    survey = Survey.objects.filter(name=self.survey_name).first()
    options = self.options
    completed = self.completed
    followups = self.followups
    if survey:
      options = [o.populate(user, survey) for o in options]
      answers = []
      for option in options:
        if option.populate(user, survey).selected:
          answers.append(option)
          completed = False
      followups = [f.populate(answers) for f in followups]
    return ContentSurvey(
      self.survey_name,
      options,
      followups,
      completed,
      self.subtitle,
      self.hide_graph
    )
  
  def find_option_key(self, option_name):
    for option in self.options:
      if option.option_name == option_name:
        return option.option_key
    return None

class ContentSurveyOption:
  def __init__(self, option_name, option_key, colour, free_text=False, selected=False, total=0):
    self.option_name = option_name
    self.option_key = option_key
    self.colour = colour
    self.free_text = free_text
    self.selected = selected
    self.total = total

  def populate(self, user, survey):
    option = SurveyOption.objects.filter(survey=survey, name=self.option_name).first()
    total = self.total
    if option:
      total = SurveyResult.objects.filter(option=option).count() + 5

    return ContentSurveyOption(
      self.option_name,
      self.option_key,
      self.colour,
      self.free_text,
      self.selected,
      total
    )

class ContentSurveyFollowup:
  def __init__(self, answers, body_key, visible=False):
    self.raw_answers = answers
    self.answers = ";".join(answers)
    self.body_key = body_key
    self.visible = visible

  def populate(self, answers):
    return ContentSurveyFollowup(
      self.raw_answers,
      self.body_key,
      not self.raw_answers or any(answer in self.raw_answers for answer in answers)
    )

class ResultsSection:
  def __init__(
      self,
      section_name,
      personal_results_key,
      global_results_key,
      pattern_key,
      complete_key,
      uncomplete_key,
      summaries,
      complete=None,
      uncomplete=None,
      take_max=5
    ):
    self.section_name = section_name
    self.personal_results_key = personal_results_key
    self.global_results_key = global_results_key
    self.pattern_key = pattern_key
    self.complete_key = complete_key
    self.uncomplete_key = uncomplete_key
    self.summaries = summaries
    self.complete = complete or []
    self.uncomplete = uncomplete or []
    self.take_max = take_max

  def populate(self, user, checklist):
    summaries = [summary.populate(user, self.take_max * 2) for summary in self.summaries]

    most_common = []
    least_common = []
    for summary in summaries:
      if not summary.exclude_from_common:
        most_common += summary.most_common_options
        least_common += summary.least_common_options

    print(most_common)
    print(least_common)
    
    most_common = [checklist.find_option_key(x[0]) for x in sorted(most_common, key=lambda x: x[1], reverse=True)[:self.take_max]]
    least_common = [checklist.find_option_key(x[0]) for x in sorted(least_common, key=lambda x: x[1])[:self.take_max]]

    print(most_common)
    print(least_common)

    return ResultsSection(
      self.section_name,
      self.personal_results_key,
      self.global_results_key,
      self.pattern_key,
      self.complete_key,
      self.uncomplete_key,
      summaries,
      most_common,
      least_common,
      self.take_max
    )
  
  def find_option_key(self, option_name):
    return None

class SurveySummary:
  def __init__(
      self,
      survey_name,
      title_key,
      level_thresholds,
      level_message_keys,
      excluded_options=None,
      global_level=0,
      most_common_options=None,
      least_common_options=None,
      exclude_from_common=False
  ):
    self.survey_name = survey_name
    self.title_key = title_key
    self.level_thresholds = level_thresholds
    self.level_message_keys = level_message_keys
    self.excluded_options = excluded_options or []
    self.global_level = global_level
    self.most_common_options = most_common_options
    self.least_common_options = least_common_options
    self.exclude_from_common = exclude_from_common

  def get_data(self, lang):
    return {
      "title": translator.t(self.title_key, lang),
      "thresholds": self.level_thresholds,
      "excluded": self.excluded_options
    }

  def populate(self, user, take_max):
    filtered_survey_result = SurveyResult.objects.exclude(option__name__in=self.excluded_options).filter(option__survey__name=self.survey_name)

    global_option_count = filtered_survey_result.count()
    total_submissions = SurveySubmission.objects.filter(survey__name=self.survey_name).count()

    print(f"{self.survey_name} = {global_option_count} / {total_submissions}")

    average_global_options = global_option_count / max(total_submissions, 1)
    global_level = 0
    for level_threshold in self.level_thresholds:
      if average_global_options < level_threshold:
        break
      global_level += 1

    option_count_query = SurveyOption.objects.exclude(name__in=self.excluded_options).filter(survey__name=self.survey_name)
    option_count_query = option_count_query.values('name')
    option_count_query = option_count_query.annotate(ocount=Count('surveyresult'))

    most_common_options = [(o["name"], o["ocount"]) for o in option_count_query.order_by('-ocount')[:take_max]]
    least_common_options = [(o["name"], o["ocount"]) for o in option_count_query.order_by('ocount')[:take_max]]

    return SurveySummary(
      survey_name=self.survey_name,
      title_key=self.title_key,
      level_thresholds=self.level_thresholds,
      level_message_keys=self.level_message_keys,
      excluded_options=self.excluded_options,
      global_level=global_level,
      most_common_options=most_common_options,
      least_common_options=least_common_options,
      exclude_from_common=self.exclude_from_common
    )

