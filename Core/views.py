from django.views.generic import View
from django.views.generic.edit import ModelFormMixin
from .models import Project, Member
from django.shortcuts import render, redirect
from .forms import ContactUsForm
from django.contrib import messages


class IndexView(View):

    http_method_names = [u'get', u'post']

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'index.html', context=context)

    def post(self, request):
        form_data = request.POST
        contact_form = ContactUsForm(form_data)
        context = self.get_context_data()
        is_form_valid = contact_form.is_valid()
        if is_form_valid:
            contact_form.save()
            message = 'Message submitted successfully!'
            messages.add_message(request, messages.SUCCESS, message=message)
            return redirect('/', context)
        messages.add_message(request, messages.INFO,
                             'Some fields in the form were missing!')
        context['contact_form'] = contact_form
        return redirect('/', context)

    def get_context_data(self, **kwargs):
        projects = Project.objects.order_by('-completion_year')
        context = kwargs
        contact_form = ContactUsForm()
        # make projects list for Portfolio section
        i = 0
        if len(projects) > 3:
            project_lists = [projects[i*3: i*3 + 3] for i in
                             range(len(projects) / 3)]
            project_lists.append(projects[i*3 + 3:])
        else:
            project_lists = [projects, ]

        # make members list for Member section
        i = 0
        members = Member.objects.filter(is_alumni=False).order_by('name')
        if len(members) > 6:
            members_lists = [members[i*6: i*6 + 6] for i in range(len(members) / 6)]
            members_lists.append(members[i*6 + 6:])
        else:
            members_lists = [members, ]

        i = 0
        alumni = Member.objects.filter(is_alumni=True).order_by('name')
        if len(alumni) > 12:
            alumni_lists = [alumni[i: i + 12] for i in range(len(alumni) / 12)]
            alumni_lists.append(alumni[i + 12:])
        else:
            alumni_lists = [alumni, ]
        i = 0
        if len(alumni_lists) > 2:
            nested_alumni_lists = [alumni_lists[i: i + 2] for
                                   i in range(len(alumni_lists) / 2)]
            nested_alumni_lists.append(alumni_lists[i + 2:])
        else:
            nested_alumni_lists = [alumni_lists, ]

        context['projects'] = project_lists
        context['members'] = members_lists
        context['alumni'] = alumni
        context['contact_form'] = contact_form

        return context

