import itertools

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project, Candidate, Team

# Create your views here.

all_projects = Project.objects.all()


def proj_overlap(project, all_projects):
    start = project.start_date
    end = project.end_date

    overlap_projects = []

    for p in all_projects:
        if (start <= p.end_date and end >= p.start_date):
            overlap_projects += p

    return overlap_projects

def total_rate(team):
    total = 0
    for candidate in team:
        total += candidate.rate

    return total

def avg_exp(team):
    total = 0
    for candidate in team:
        total += candidate.years_exp

    return total / len(team)


def matched_team(slug):
    #   1) Find available candidates
    #      - If a candidate is assigned to a project that conflicts with the one we are concerned with, they are not considered
    #   2) for skill in candidate.skills if candidates_skills in required_skills then add to consideration
    #   3) Find all the combinations of size n that meet the skill requirements starting from n=1 and going up until you have several team options
    #   4) Find the min/max of target attributes (price, experience, etc)
    project = Project.objects.get(slug=slug)
    all_candidates = Candidate.objects.all()
    # candidate will return object <Candidate: Name (index)>
    # >>> emily = Candidate.objects.get(first_name="Emily")
    # >>> emily.first_name
    # 'Emily'
    # >>> emily_projects = emily.current_proj.all()
    # >>> emily_projects
    # returns -> <QuerySet [<Project: Project 1>]>
    # >>> emily_projects[0]
    # >>> emily_projects[0].name
    # 'Emily'
    # <Project: Project 1> == <Project: Project 1>
    # candidate.current_proj.all()
    # returns <QuerySet [<Project: Project 1>]>
    overlap_projects = proj_overlap(project, all_projects)

    for i, candidate in enumerate(all_candidates):
        if candidate.project.all() in overlap_projects and candidate.skills.all() not in project.skills_req.all():
            all_candidates.pop(i)

    valid_combos = []
    for j in range(1, 5):
        combos = itertools.combinations(all_candidates, j)
        total_skills = []
        valid = True
        for combo in combos:
            for candidate in combo:
                total_skills += candidate.skills.all()
            for skill in project.skills_req.all():
                if skill not in total_skills:
                    valid = False
            if valid:
                Team.objects.create(members=combo, total_skills=total_skills,
                                    avg_experience=avg_exp(combo),total_rate=total_rate(combo))


def index(request):
    return render(request, 'team_finder/index.html')


class ProjectsView(ListView):
    model = Project
    template_name = 'team_finder/projects.html'
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'team_finder/project-detail.html'
    # def get_context_data(self, **kwargs):
    #     context = super(ProjectDetail, self).get_context_data(**kwargs)
    #     context['tasks'] = Task.objects.filter(list=self.object)
    #     return context

class CandidatesView(ListView):
    model = Candidate
    template_name = 'team_finder/candidates.html'
    context_object_name = 'candidates'
