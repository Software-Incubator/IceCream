from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30, default="user")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, default="unspecified")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='./static/images', null=True)

    class Meta:
        ordering = ["-timestamp"]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
