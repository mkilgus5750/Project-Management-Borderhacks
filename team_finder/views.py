from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project, Candidate

# Create your views here.

def index(request):
    return render(request, 'team_finder/index.html')

class ProjectsView(ListView):
    model = Project
    template_name = 'team_finder/projects.html'
    context_object_name = 'projects'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'team_finder/project-detail.html'

class CandidatesView(ListView):
    model = Candidate
    template_name = 'team_finder/candidates.html'
    context_object_name = 'candidates'