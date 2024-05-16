from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponse
import markdown
import self_checklist_proto.templatetags
from .content import checklists, screen_sets
import json
from .models import *


def int_or_else(x, or_else):
  try:
    return int(x)
  except:
    return or_else

def get_lang(request):
  lang = "en"
  if request.user.is_authenticated:
    user_settings = UserSettings.objects.filter(user=request.user).first()
    if user_settings and user_settings.language:
      lang = user_settings.language

  if "lang" in request.GET:
    lang = request.GET["lang"]
  
  return lang

def checklist(request, name=None):
  if name in checklists:
    checklist = checklists[name]
    lang = get_lang(request)
    checklist = checklist.populate(request.user)

    return render(request, "checklist.html", {
      "checklist": checklist,
      "lang": lang,
      "qlang": request.GET.get("lang"),
      "checklist_name": name
    })
  else:
    return HttpResponseNotFound()

def checklist_section(request, checklist_name=None, section_name=None):
  if checklist_name not in checklists:
    return HttpResponseNotFound()
  
  checklist = checklists[checklist_name]
  sections = [x for x in checklist.sections if x.section_name == section_name]
  if len(sections) == 0:
    return HttpResponseNotFound()

  lang = get_lang(request)
  section = sections[0]
  section = section.populate(request.user)

  surveys = [item.content for item in section.items if item.content.content_type == "survey"]
  pie_data = {
    survey.survey_name: survey.get_data(lang) for survey in surveys
  }

  return render(request, "section.html", {
    "section": section,
    "lang": lang,
    "qlang": request.GET.get("lang"),
    "checklist_name": checklist_name,
    "finish_url": f"/checklist/{checklist_name}",
    "pie_data": pie_data
  })

def render_screen(request, name):
  if name in screen_sets:
    screen_set = screen_sets[name]
    lang = get_lang(request)

    return render(request, "screens.html", {
      "screens": screen_set.screens,
      "lang": lang,
      "qlang": request.GET.get("lang"),
      "selected_screen": int_or_else(request.GET.get("page", 1), 1),
      "finish_url": screen_set.finish_url
    })
    
  else:
    return HttpResponseNotFound()


def introduction(request):
  return render_screen(request, "introduction")


def submit_survey(request, name=None):
  if not name:
    return HttpResponseBadRequest()

  if request.method == "POST":
    json_data = json.loads(request.body)
    print(json_data)
    
    survey = Survey.objects.filter(name=name).first()
    if not survey:
      survey = Survey(name=name)
      survey.save()

    if "answers" not in json_data:
      return HttpResponseBadRequest()

    for option_name, selected in json_data["answers"].items():
      option = SurveyOption.objects.filter(survey=survey, name=option_name).first()
      if not option:
        option = SurveyOption(survey=survey, name=option_name)
        option.save()

      if selected:
        result = SurveyResult(option=option)
        result.save()
      
    return HttpResponse(status=204)
  else:
    return HttpResponseNotFound()

