from django.views.generic import View, FormView, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from email.mime.image import MIMEImage
# from django.core.urlresolvers import reverse_lazy

from .forms import RegistrationForm, ContactUsForm, RegistrationAlumni
from .models import Project, Member, ContactInfo, Blog, Event, ContactUs, Registration, \
 EmailContent, EmailAttachment, AlumniRegistration
from IceCream.settings.base import RECEIVER_EMAIL, EMAIL_HOST_USER

import json


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
        members = Member.objects.filter(is_alumni=False).order_by('batch', 'name')
        if len(members) > 6:
            members_lists = [members[i * 6: i * 6 + 6] for i in range(int(len(members) / 6))]
            i = int(len(members) / 6) - 1
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
            subject = subject
            message_to_show = name + 'has registered'
            details = render_to_string('email_template.html', {
                'name': name,
                'email': email,
                'contact': contact,
                'message': message,
                'subject': subject,
            })

            from_mail = EMAIL_HOST_USER
            to_mail = (RECEIVER_EMAIL,)
            send_mail(subject, message_to_show, from_mail, to_mail, html_message=details, fail_silently=False)

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
            event_receiver_email = form.cleaned_data['college_email']
            person = form.cleaned_data['name']
            registration = form.save()

            allowed = False

            try:
                allowed = (EmailContent.objects.get(event=self.event)).mail_allowed
            except EmailContent.DoesNotExist:
                pass

            if allowed:
                content = EmailContent.objects.get(event=self.event)
                all_files = EmailAttachment.objects.filter(event=self.event)

                subject = content.subject
                message = render_to_string('registration-response-email.html', {
                    'content': content,
                    'event': self.event,
                    'name': person,
                })
                
                from_mail = EMAIL_HOST_USER
                # to_mail = ['ankit1911006@akgec.ac.in']
                to_mail = [event_receiver_email]

                mail = EmailMessage(subject, message, from_mail, to_mail)
                mail.content_subtype = "html"
                mail.mixed_subtype = 'related'

               # image_sub_type = (str(self.event.pic_path).split('.'))[-1]
               # event_image = MIMEImage(self.event.pic_path.read(), _subtype=image_sub_type)
               # event_image.add_header('Content-ID', '<{}>'.format(self.event.pic_path))
               # mail.attach(event_image)

                for single_file in all_files:
                    mail.attach(filename=single_file.name,
                                content=single_file.files.read())
                #adding mail sent status
                try:
                    mail.send(fail_silently=False)
                    registration.mail_sent_status = True
                    registration.save()
                except:
                    pass
                
                ##############
            messages.add_message(request, messages.SUCCESS,
                                 "Please check your email.")
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
                                 "Registrations for event are not active!")
            return redirect(reverse_lazy('home'))


class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return render(request, self.template_name, context={'blogs': blogs})


class BlogDetailView(View):
    template_name = "blog_detail.html"

    def get(self, request, pk, *args,**kwargs):
        blog = get_object_or_404(Blog,pk=pk)
        context = {
            'blog':blog
        }

        return render(request, self.template_name, context=context)

class FeedbackView(View):
    template_name = "feedback.html"

    def get(self, request, *args,**kwargs):
        return render(request, self.template_name)


# class AlumniRegistrationView(View):
#     template_name = "alumni-registration.html"

#     def post(self,request,*args,**kwargs):
#         form = RegistrationAlumni(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             return render(request,self.template_name,{'form':form,'message':"error"})

#     def get(self,request,*args,**kwargs):
#         form = RegistrationAlumni()
#         return render(request,self.template_name,{'form':form})


class AlumniView(View):
    template_name = "alumni_profile.html"

    def get(self, request, slug, batch, *args, **kwargs):
        alumni = get_object_or_404(Member, slug__iexact=slug, batch=batch, is_alumni=True)
        context = {
            'alumnus': alumni
        }
        return render(request, self.template_name, context)


def view404(request, exception):
    error_code = 404
    error_message = 'Page Not Found'
    return render(request, '404.html', {'error_code':error_code, 'error_message':error_message})


def view500(request):
    error_code = 500
    error_message = 'Internal Server Error'
    return render(request, '404.html', {'error_code':error_code, 'error_message':error_message})


class EmailTemplatesView(View):
    template_name = "registration-response-email.html"

    def get(self, request, *args, **kwargs):
        event_id = request.GET.get('event')
        event = get_object_or_404(Event, id=event_id)
        content = EmailContent.objects.get(event=event)
        subject = content.subject
        ctx = {
            'content': content,
            'event': event,
            'name': "Utkarsh",
        }
        return render(request, self.template_name, ctx )
