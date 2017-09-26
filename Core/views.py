from django.views.generic import View, FormView, CreateView
from .models import Project, Member, ContactInfo
from django.shortcuts import render, redirect
from .forms import ContactUsForm, RegistrationForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from .models import Event, Blog


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
        event = Event.objects.filter(active=True).first()
        contact_form = ContactUsForm()
        contact_info = ContactInfo.objects.filter(active=True)
        # make projects list for Portfolio section
        i = 0
        if len(projects) > 3:
            project_lists = [projects[i * 3: i * 3 + 3] for i in
                             range(len(projects) / 3)]
            project_lists.append(projects[i * 3 + 3:])
        else:
            project_lists = [projects, ]

        # make members list for Member section
        i = 0
        members = Member.objects.filter(is_alumni=False).order_by('batch','name')
        if len(members) > 6:
            members_lists = [members[i * 6: i * 6 + 6] for i in range(len(members) / 6)]
            members_lists.append(members[i * 6 + 6:])
        else:
            members_lists = [members, ]

        i = 0
        alumni = Member.objects.filter(is_alumni=True).order_by('-batch')
        if len(alumni) > 12:
            alumni_lists = [alumni[i * 12: i * 12 + 12] for i in range(len(alumni) / 12)]
            alumni_lists.append(alumni[i * 12 + 12:])
        else:
            alumni_lists = [alumni, ]
        i = 0
        if len(alumni_lists) > 2:
            nested_alumni_lists = [alumni_lists[i * 2: i * 2 + 2] for
                                   i in range(len(alumni_lists) / 2)]
            nested_alumni_lists.append(alumni_lists[i * 2 + 2:])
        else:
            nested_alumni_lists = [alumni_lists, ]

        context['projects'] = project_lists
        context['members'] = members_lists
        context['alumni'] = nested_alumni_lists
        context['contact_form'] = contact_form
        context['event'] = event
        context['contact_info'] = contact_info

        print(contact_info[0].contact_number)

        return context


class RegistrationView(FormView):
    template_name = 'registration.html'

    success_url = reverse_lazy('home')

    form_class = RegistrationForm

    event = Event.objects.filter(active=True).first()

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully registered.")
            return redirect(reverse_lazy('home'))
        return render(request, 'registration.html', {'form': form, 'event': self.event})

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()

        context = {
            'form': form,
            'event': self.event
        }
        return render(request, 'registration.html', context)


class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(request, self.template_name, context={'blogs': blogs})
