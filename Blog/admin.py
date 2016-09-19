from django.contrib import admin

from .models import *
from django_summernote.widgets import SummernoteWidget


# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget(attrs={'cols': 30, 'rows': 20})}
    }
    list_display = ("title", "updated", "created_on", "author", "category")
    list_display_links = ["updated"]
    list_filter = ['updated', 'created_on']
    search_fields = ["title", "content", "created_on"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)

admin.site.register(Category)
