from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project

# Create your views here.

def index(request):
    return render(request, 'team_finder/index.html')

class ProjectsView(ListView):
    model = Project
    template_name = 'team_finder/index.html'
    context_object_name = 'projects'