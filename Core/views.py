from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Project, Member


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        projects = Project.objects.order_by('-completion_year')
        context = super(IndexView, self).get_context_data(**kwargs)

        # make projects list for Portfolio section
        i = 0
        if len(projects) > 3:
            project_lists = [projects[i: i+3] for i in range(len(projects)/3)]
            project_lists.append(projects[i+3:])
        else:
            project_lists = [projects, ]

        # make members list for Member section
        i = 0
        members = Member.objects.filter(is_alumni=False).order_by('name')
        if len(members) > 6:
            members_lists = [members[i: i+6] for i in range(len(members)/6)]
            members_lists.append(members[i+6:])
        else:
            members_lists = [members, ]

        i = 0
        alumni = Member.objects.filter(is_alumni=True).order_by('name')
        if len(alumni) > 12:
            alumni_lists = [alumni[i: i+12] for i in range(len(alumni)/12)]
            alumni_lists.append(alumni[i+12:])
        else:
            alumni_lists = [alumni, ]
        i = 0
        if len(alumni_lists) > 2:
            nested_alumni_lists = [alumni_lists[i: i+2] for
                                   i in range(len(alumni_lists)/2)]
            nested_alumni_lists.append(alumni_lists[i+2:])
        else:
            nested_alumni_lists = [alumni_lists, ]

        context['projects'] = project_lists
        context['members'] = members_lists
        context['alumni'] = nested_alumni_lists

        return context
