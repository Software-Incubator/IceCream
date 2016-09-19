from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views.generic import DetailView, ListView
from django.contrib import messages


# Create your views here.

class PostDetail(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'


class PostsByTag(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        category = Post.objects.get(pk=self.kwargs['pk']).category
        self.queryset = Post.objects.filter(category=category)
        # self.queryset = Post.objects.filter(category=self.args[0])

        return self.queryset


class SearchView(ListView):
    context_object_name = 'search_results'
    template_name = 'search_view.html'

    def get(self, request, *args, **kwargs):
        return super(SearchView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        query_string = self.request.POST['search']
        queryset = Post.objects.filter(title__icontains=query_string)
        return queryset
