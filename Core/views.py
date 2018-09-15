from django.views.generic import View, FormView, CreateView
from .models import Project, Member, ContactInfo, Blog, Event, ContactUs, Registration
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactUsForm, RegistrationForm
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
import json
from django.http import HttpResponse, JsonResponse


class IndexView(View):
    http_method_names = [u'get', u'post']

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'index.html',context)

    def get_context_data(self, **kwargs):

        # getting all the projects
        projects = Project.objects.order_by('-completion_year')

        context = kwargs
        event = Event.objects.filter(active=True).first()
        contact_form = ContactUsForm()
        contact_info = ContactInfo.objects.filter(active=True)

        # make members list for Member section
        i = 0
        members = Member.objects.filter(is_alumni=False).order_by('batch','name')
        if len(members) > 6:
            members_lists = [members[i * 6: i * 6 + 6] for i in range(int(len(members) / 6))]
            members_lists.append(members[i * 6 + 6:])
        else:
            members_lists = [members, ]

        alumni = Member.objects.filter(is_alumni=True).order_by('-batch')

        # context['projects'] = project_lists
        context['projects'] = projects
        context['members'] = members_lists
        context['alumni'] = alumni
        context['contact_form'] = contact_form
        context['event'] = event
        context['contact_info'] = contact_info
        return context


class SaveContactView(View):

    def get(self, request):
        data_to_frontend = dict()
        contact_us = None
        name = request.GET['name']
        email = request.GET['email']
        contact = request.GET['contact']
        message = request.GET['message']
        subject = request.GET['subject']
        if name == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'Name cannot be empty..'
        elif email == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'Email cannot be empty..'
        elif contact == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'contact cannot be empty..'
        elif message == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'message cannot be empty..'
        elif subject == '':
            data_to_frontend['done'] = 0
            data_to_frontend['message'] = 'subject cannot be empty..'
        else:
            try:
                contact_us = ContactUs.objects.create(name=name, contact=contact, email=email, subject=subject, message=message)
            except:
                data_to_frontend['done'] = 0
                data_to_frontend['message'] = 'Request failed due to internal error.'

        if contact_us:
            data_to_frontend['done'] = 1
            data_to_frontend['message'] = 'Request successfully registered.'

        return JsonResponse(data_to_frontend)


class RegistrationView(FormView):
    template_name = 'registration.html'

    success_url = reverse_lazy('home')

    form_class = RegistrationForm
    
    event = Event.objects.filter(active=True).first()

    def post(self, request, *args, **kwargs):
        alert = ''
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Successfully registered.")
            return redirect(reverse_lazy('registration'))
        else:
            if '__all__' in dict(form.errors):
                alert = dict(form.errors)['__all__']
            return render(request, 'registration.html', {'form': form, 'event': self.event, 'alert':alert})

    def get(self, request, *args, **kwargs):
        if self.event:
            form = self.form_class()

            context = {
                'form': form,
                'event': self.event
            }
            return render(request, 'registration.html', context)
        else:
            messages.add_message(request, messages.SUCCESS,
                                 "No event active at present")
            return redirect(reverse_lazy('home'))


class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(request, self.template_name, context={'blogs': blogs})


class BlogDetailView(View):
    template_name = "blog_detail.html"

    def get(self,request,pk, *args,**kwargs):
        blog = get_object_or_404(Blog,pk=pk)
        context = {
            'blog':blog
        }
        
        return render(request, self.template_name, context=context)


def view404(request):
    error_code = 404
    error_message = 'Page Not Found'
    return render(request, '404.html', {'error_code':error_code, 'error_message':error_message})

def view500(request):
    error_code = 500
    error_message = 'Internal Server Error'
    return render(request, '404.html', {'error_code':error_code, 'error_message':error_message})