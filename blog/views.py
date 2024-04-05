from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from .models import Post
# Create your views here.


def index(request):
    latest_articles = Post.objects.all().order_by("-date")[:3]
    # latest_articles = sorted(all_posts, key=lambda x: x.date, reverse=True)
    return render(request, "blog/index.html", {"articles": latest_articles})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {"articles": all_posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post = next(x for x in all_posts if x.slug == slug)
    return render(request, "blog/post_detail.html", {"post": post, "tags": post.tags.all()})
