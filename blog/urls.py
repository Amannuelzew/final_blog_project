from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post_detail"),
    path("posts/favorite/", views.FavoriteView.as_view(), name="favorite_post"),
    path("posts/stored/", views.StoredView.as_view(), name="stored_posts"),
    #path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
]
