from __future__ import unicode_literals

import os
import uuid
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField

#from ckeditor_uploader.fields import RichTextUploadingField

from django.core.validators import RegexValidator,FileExtensionValidator
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
# DO NOT DELETE THIS FUNCTION
# If you think that this function is outright useless because it is never called,
# stop right there. You delete this and all the migrations will FAIL!


def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)


def members_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/members', filename)


def projects_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/projects', filename)


def events_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/events', filename)


def event_validator(value):
    if value is True and Event.objects.filter(active=True).count() >= 1:
        raise ValidationError(
            'More than one events cannot be active at a given time'
        )


class Event(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, validators=[event_validator, ])
    pic_path = models.FileField(upload_to=events_upload_location, null=True,
                                default=None)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'contact us'


class Designation(models.Model):
    name = models.CharField(max_length=225, unique=True, null=False,
                            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Designations"


class Technology(models.Model):
    name = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Member(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    designation = models.ForeignKey(to=Designation, null=True,on_delete= models.CASCADE)
    technology = models.ManyToManyField(to=Technology)
    presently_at = models.CharField(max_length=225, null=False, blank=True)
    is_alumni = models.BooleanField(default=False)
    batch = models.IntegerField(null=False)
    pic_path = models.FileField(upload_to=members_upload_location, null=True,
                                default=None)
    facebook = models.CharField(max_length=225, null=True, default=None)
    github = models.CharField(max_length=225, null=True, default=None)
    linkedin = models.CharField(max_length=225, null=True, default=None)
 
    testimonial = models.TextField(max_length=500, null=True, blank=True, default=None)
    message = models.TextField(max_length=500, null=True, default='LOVE-PEACE-CODE')
    email = models.EmailField(max_length=225, null=True, blank=True, default=None)
    phone = models.CharField(max_length=10, null=True, blank=True, default=None)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " | " + str(
            self.batch) + " | " + self.designation.name

    class Meta:
        verbose_name_plural = "Members"
        ordering = ['batch']


class Project(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    description = models.CharField(max_length=225, null=False, blank=False)
    completion_year = models.IntegerField(null=True, default=None)
    image_path = models.FileField(upload_to=projects_upload_location, null=True,
                                  default=None)

    def __str__(self):
        return self.name + str(self.completion_year)

    class Meta:
        verbose_name_plural = "Projects"


class Branch(models.Model):
    name = models.CharField(max_length=10, null=False)
    active = models.BooleanField(default=True)
    code = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Branches'


class Year(models.Model):
    class year_choices(models.IntegerChoices):
        First = 1 , _('1st year')
        Second = 2, _('2nd year')
        Third = 3, _('3rd year')
        Forth = 4,_('4th year')
    value = models.IntegerField(choices=year_choices.choices)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.get_value_display())

    class Meta:
        ordering = ['value',]


def student_number_validator(value):
    if Registration.objects.filter(student_number=value,
                                   event=Event.objects.filter(
                                           active=True).first()).exists():
        raise ValidationError(
            'Student number already registered!'
        )

class Registration(models.Model):
    # experience_choices = [
    #     ('no','No Experience'),
    #     ('beginner',"Beginner"),
    #     ('intermediate','Intermediate'),
    #     ('expert','Expert')
    # ]

    name = models.CharField(max_length=100, null=False)
    college_email = models.EmailField(unique=True)
    # roll_no = models.CharField(max_length=13,default="123")
    #changing just for first year registration
    roll_no = models.CharField(max_length=13, null=True)
    student_number = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10, null=False)
    branch = models.ForeignKey('Branch',on_delete=models.CASCADE)
    gender = models.ForeignKey('Gender',default=1,related_name='registrations',on_delete=models.CASCADE)
    # year = models.ForeignKey('Year',default=2,on_delete=models.CASCADE)
    # domain = models.ForeignKey('Domain',default=1,related_name='registrations',on_delete=models.CASCADE)
     # Default Year is 1 for SI Workshop
    year = models.ForeignKey('Year',default=1,on_delete=models.CASCADE)
    # Registration for workshop doesn't require Domain so Null=True
    domain = models.ForeignKey('Domain',related_name='registrations',on_delete=models.CASCADE, null=True)
    skills = models.CharField(max_length=250,default="HTML",help_text='Skills like HTML, CSS, Java...')
    hacker_rank_username = models.CharField(max_length=250,null=True,blank=True,help_text='Your HackerRank username. Please create an account on HackerRank.')
    timestamp = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    your_work = models.TextField(blank=True,null=True,help_text='Links to your work or coding profiles.')
    is_hosteler = models.BooleanField(default=False)
    mail_sent_status = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    # whatsapp = models.CharField(max_length=10, default="9999999999", null=False)
    # experience = models.CharField(choices=experience_choices,max_length=20,null=False,blank=False)
    # account_handles = models.CharField(max_length=500, blank=True)
    # about_yourself = models.TextField(max_length=500, blank=True)
    # why_attend = models.TextField(max_length=500, blank=True)
    # design_tools = models.TextField(max_length=500,default="",blank=True)
    # insta_improvement = models.TextField(blank=False,null=False)
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.event = Event.objects.filter(active=True).first()
        super(Registration, self).save()

    def __str__(self):
        return "{} || {} || {}".format(self.name, self.branch, str(self.year))


class Domain(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    active = models.BooleanField(default=False)
    member_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "contact_information"

    def __str__(self):
        return self.member_name


class Blog(models.Model):
    title = models.CharField(max_length=80, blank=False, null=False)
    author = models.CharField(max_length=30,blank=False,null=False)
    content = RichTextUploadingField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog_detail',kwargs={'pk':self.pk})


    def __str__(self):
        return "{} | {}".format(self.title, self.author)


class EmailContent(models.Model):
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    mail_allowed = models.BooleanField(default=False)
    subject = models.CharField(max_length=100)
    text = RichTextField()

    def __str__(self):
        return self.event.name


class EmailAttachment(models.Model):
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    files = models.FileField(   
                                upload_to=events_upload_location, null=True,default=None,
                                validators=[FileExtensionValidator(['pdf'])]
                            )
    name = models.CharField(max_length=80, blank=False)
    def save(self, *args, **kwargs):
        if self.name[-4:]!='.pdf':
            self.name += '.pdf'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.event.name + "  " + self.name


class AlumniRegistration(models.Model):
    choice = (
         ('22 September(Sunday)','22 September(Sunday)'),
         ('29 September(Sunday)','29 September(Sunday)'),
         ('2  October(Wednesday)','2 October(Wednesday)'),
     )
    name = models.CharField(max_length=200)
    batch = models.CharField(max_length=4)
    phone_regex = RegexValidator(regex=r"^[56789]\d{9}$")
    contact_no = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)
    message = models.CharField(max_length=500,blank=True,null=True)
    date = models.CharField(max_length=200,choices=choice,blank=True,null=True)

    def __str__(self):
        return self.name
