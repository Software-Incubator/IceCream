from __future__ import unicode_literals
from django.db import models


def upload_location(instance, filename):
    return '%s/%s' %(instance.id, filename)


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)


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
    designation = models.ForeignKey(to=Designation, null=True)
    technology = models.ManyToManyField(to=Technology)
    presently_at = models.CharField(max_length=225, null=False, blank=True)
    is_alumni = models.BooleanField(default=False)
    batch = models.IntegerField(null=False)
    pic_path = models.FileField(upload_to=upload_location, null=True, default=None)
    facebook = models.CharField(max_length=225, null=True, default=None)
    github = models.CharField(max_length=225, null=True, default=None)
    linkedin = models.CharField(max_length=225, null=True, default=None)


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
    image_path = models.FileField(upload_to=upload_location, null=True, default=None)

    def __str__(self):
        return self.name + str(self.completion_year)

    class Meta:
        verbose_name_plural = "Projects"


# class Branch(models.Model):
#     name = models.CharField(max_length=3, null=False)
#
#     def __str__(self):
#         return self.name


class Registration(models.Model):
    name = models.CharField(max_length=225, null=False)
    email = models.EmailField(unique=True)
    contact = models.BigIntegerField()
    student_number = models.IntegerField(unique=True)
    branch = models.CharField(max_length=3)
    year = models.IntegerField()
    gender = models.CharField(max_length=1)
    hosteler = models.BooleanField(default=False)
    designer = models.BooleanField(default=False)

    def __str__(self):
        return "{} || {} || {}".format(self.name, self.branch, str(self.year))


