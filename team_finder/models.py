from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Skill(models.Model):
    name = models.CharField(null=True, max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    skills_req = models.ManyToManyField(Skill)
    slug = models.SlugField(null=True, db_index=True)
    def __str__(self):
        return self.name

class Candidate(models.Model):
    first_name =  models.CharField(max_length=100)
    slug = models.SlugField(null=True, db_index=True)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    rate = models.FloatField()
    years_exp = models.IntegerField()
    skills = models.ManyToManyField(Skill)
    current_proj = models.ManyToManyField(Project)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Team(models.Model):
    members = models.ManyToManyField(Candidate)
    avg_experience = models.FloatField()
    total_rate = models.FloatField()
    total_skills = models.ManyToManyField(Skill)

