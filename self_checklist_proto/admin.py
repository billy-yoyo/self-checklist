from django.contrib import admin
from .models import *

class SurveyAdmin(admin.ModelAdmin):
  list_display = ["name"]

class SurveyOptionAdmin(admin.ModelAdmin):
  list_display = ["name", "survey"]

class SurveyResultAdmin(admin.ModelAdmin):
  list_display = ["option"]

admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyOption, SurveyOptionAdmin)
admin.site.register(SurveyResult, SurveyResultAdmin)
