import itertools

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project, Candidate, Team, Skill
from django.core import serializers

# Create your views here.

all_projects = Project.objects.all()

def proj_overlap(project, all_projects):
    start = project.start_date
    end = project.end_date

    overlap_projects = []

    #print(all_projects)

    for p in all_projects:
        if (start <= p.end_date and end >= p.start_date):
            overlap_projects += [p]

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

def matched_team(project):
    #   1) Find available candidates
    #      - If a candidate is assigned to a project that conflicts with the one we are concerned with, they are not considered
    #   2) for skill in candidate.skills if candidates_skills in required_skills then add to consideration
    #   3) Find all the combinations of size n that meet the skill requirements starting from n=1 and going up until you have several team options
    #   4) Find the min/max of target attributes (price, experience, etc)
    # project = Project.objects.get(slug=slug)
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
        if candidate.current_proj.all() in overlap_projects and candidate.skills.all() not in project.skills_req.all():
            all_candidates.pop(i)

    count = 0
    for j in range(1, 8):
        if count >= 10:
            break
        print(j)
        combos = itertools.combinations(all_candidates, j)
        for combo in combos:
            total_skills = []
            valid = True
            for candidate in combo:
                total_skills += candidate.skills.all()
            for skill in project.skills_req.all():
                if skill not in total_skills:
                    valid = False
            if valid:
                print('SUCCESS')
                count += 1
                new_team = Team(avg_experience=avg_exp(combo), total_rate=total_rate(combo))
                new_team.save()

                for s in total_skills:
                    new_team.total_skills.add(s)
                for m in combo:
                    new_team.members.add(m)
            else:
                pass
                print('INVALID')
                print('needed: ' + str(project.skills_req.all()))
                print('total: ' + str(total_skills))
                print(combo)
                print('---------------')


def index(request):
    """
    data_proj = serializers.serialize("json", Project.objects.all())
    data_team = serializers.serialize("json", Team.objects.all())
    data_skil = serializers.serialize("json", Skill.objects.all())
    data_cand = serializers.serialize("json", Candidate.objects.all())

    with open('a.txt', 'w') as f:
        f.write(data_cand)
        """
    return render(request, 'team_finder/index.html', {

    })

class ProjectsView(ListView):
    model = Project
    template_name = 'team_finder/projects.html'
    context_object_name = 'projects'

class ProjectDetail(DetailView):
    model = Project
    template_name = 'team_finder/project-detail.html'
    all_projects = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        matched_team(self.object)
        return context

class CandidatesView(ListView):
    model = Candidate
    template_name = 'team_finder/candidates.html'
    context_object_name = 'candidates'
