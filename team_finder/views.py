from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project, Candidate

# Create your views here.

all_projects = Project.objects.all()

def match_team(slug):
#   1) Find available candidates
#      - If a candidate is assigned to a project that conflicts with the one we are concerned with, they not considered
#   2) for skill in candidate.skills if candidates_skills in required_skills then add to consideration
#   3) Find all the combinations of size n that meet the skill requirements starting from n=1 and going up until you have several team options
#   4) Find the min/max of target attributes (price, experience, etc)
    Project.objects.get(slug=slug)
    all_candidates = Candidate.objects.all()
    for candidate in all_candidates:
        pass


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