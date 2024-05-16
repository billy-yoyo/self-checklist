from django.db import models
from django.conf import settings

class Language(models.Model):
  full_name = models.CharField(max_length=255)
  short_code = models.CharField(max_length=255)

class UserSettings(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  language = models.ForeignKey(Language, on_delete=models.CASCADE)

class Survey(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self) -> str:
    return self.name

class SurveyOption(models.Model):
  survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)

  def __str__(self) -> str:
    return f"{self.survey}/{self.name}"

class SurveyResult(models.Model):
  option = models.ForeignKey(SurveyOption, on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return str(self.option)