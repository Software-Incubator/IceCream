from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Category
from django.views.generic import DetailView, ListView
from django.contrib import messages


# Create your views here.

# def post_create(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         messages.success(request, "Successfully Created")
#         form.save()
#     else:
#         messages.error(request, "Not Successfully Created")
#     context = {
#         "form": form,
#     }
#     return render(request, "form.html", context)

class PostDetail(DetailView):
    template_name = 'post_detail.html'

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    context_object_name = 'post'


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'


class PostsByTag(ListView):
    def get_queryset(self):
        category = Post.objects.get(pk=self.kwargs['pk']).category
        self.queryset = Post.objects.filter(category=category)
        return self.queryset

    context_object_name = 'posts'
    template_name = 'post_list.html'


class SearchView(ListView):
    def get(self, request, *args, **kwargs):
        return super(SearchView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_queryset(self):
        query_string = self.request.POST['search']
        # queryset = Post.objects.filter(content__contains=query_string)

        queryset = Post.objects.filter(title__icontains=query_string)


        return queryset

    context_object_name = 'search_results'
    template_name = 'search_view.html'
