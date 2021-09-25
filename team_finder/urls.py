from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('projects', views.ProjectsView.as_view(), name='projects'),
]