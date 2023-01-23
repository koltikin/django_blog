from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Post

# Create your views here.


def home(req):
    context = Post.objects.all()

    return render(req, "my_blog/home.html", {"posts": context, "title": "home"})


def about(req):
    return render(req, "my_blog/about.html", {"title": "About"})
