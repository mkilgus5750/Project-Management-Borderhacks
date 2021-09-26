from django.contrib import admin
from .models import Project, Skill, Candidate, Team

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CandidateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name',)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill)
admin.site.register(Team)
admin.site.register(Candidate, CandidateAdmin)