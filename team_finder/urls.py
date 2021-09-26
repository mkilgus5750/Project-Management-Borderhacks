from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetail.as_view(), name='project-detail'),
    path('candidates', views.CandidatesView.as_view(), name='candidates'),
]
from .models import Project
from .views import matched_team
all_projects = Project.objects.all()
for project in all_projects:
     matched_team(project)