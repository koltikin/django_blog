from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post

# Create your views here.


def home(req):
    context = Post.objects.all()

    return render(req, "my_blog/home.html", {"posts": context, "title": "home"})


class PostListView(ListView):
    model = Post
    template_name = (
        "my_blog/home.html"  # <app>/<moldel><viewtype>.html     my_blog/post_list.html
    )
    context_object_name = "posts"
    ordering = ["-posted_date"]
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "my_blog/user_posts.html"  # <app>/<moldel><viewtype>.html     my_blog/post_list.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-posted_date")


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(req):
    return render(req, "my_blog/about.html", {"title": "About"})
