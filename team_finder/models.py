from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class candidate(models.Model):
    full_name =  models.CharField()
    title = models.CharField()
    email = models.EmailField()
    rate = models.FloatField()
    years_exp = models.IntegerField()
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)
    current_proj = models.ForeignKey(Project, on_delete=models.CASCADE)

class Skill(models.Model):
    # TODO
    dummyvalue = models.NullBooleanField()

class Project(models.Model):
    name = models.CharField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    skills_req = models.ForeignKey(Skill, on_delete=models.CASCADE)
