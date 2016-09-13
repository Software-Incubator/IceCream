from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.



def post_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        messages.success(request, "Successfully Created")
        form.save()
    else:
        messages.error(request, "Not Successfully Created")
    context = {
        "form":form,
    }
    return render(request, "form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":instance.title,
        "instance":instance,
    }
    return render(request,"post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
       "title": "list",
    }

    return render(request, 'post_create.html', context)