from ..models import *
from ..language import translator

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
      [s.populate(user) for s in self.sections]
    )


class Progression:
  def __init__(self, steps):
    self.steps = steps

  def populate(self, user):
    return Progression([s.populate(user) for s in self.steps])

  
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

  def populate(self, user):
    return Section(self.section_name, self.title_key, [i.populate(user) for i in self.items])


class Item:
  def __init__(self, title_key, content, id=None):
    self.id = id if id is not None else counter()
    self.title_key = title_key
    self.content = content

  def populate(self, user):
    return Item(self.title_key, self.content.populate(user), self.id)
  
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
  def __init__(self, survey_name, options, followups=[], completed=False):
    super().__init__("survey")
    self.survey_name = survey_name
    self.options = options
    self.followups = followups
    self.completed = completed

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
      completed
    )

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
      any(answer in self.raw_answers for answer in answers)
    )



