from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
    #path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
]
