from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('projects', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetail.as_view(), name='project-detail'),
    path('candidates', views.CandidatesView.as_view(), name='candidates'),
]
