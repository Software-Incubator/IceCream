from __future__ import unicode_literals

from django.db import models
from Core.models import Member


class Category(models.Model):
    name = models.CharField(max_length=30, default="unspecified")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    updated = models.DateField(auto_now=True, auto_now_add=False)
    created_on = models.DateField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='./static/images', null=True)

    class Meta:
        ordering = ["-created_on"]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
