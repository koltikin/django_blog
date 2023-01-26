from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="home_page"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", views.UpdatePostView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("post/new/", views.CreatePostView.as_view(), name="post_create"),
    path("about/", views.about, name="about_page"),
]
