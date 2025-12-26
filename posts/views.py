from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    template_name = "post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"


class PostCreate(CreateView):
    model = Post
    template_name = "posts/post_new.html"
    fields = ["title", "author", "body"]


class PostUpdate(UpdateView):
    model = Post
    template_name = "posts/post_edit.html"
    fields = ["title", "body"]


class PostDelete(DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy("posts_home")
