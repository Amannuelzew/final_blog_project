from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from .forms import CommentForm
from .models import Post,Comment
# Create your views here.


def index(request):
    latest_articles = Post.objects.all().order_by("-date")[:3]
    # latest_articles = sorted(all_posts, key=lambda x: x.date, reverse=True)
    return render(request, "blog/index.html", {"articles": latest_articles})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {"articles": all_posts})


def post_detail(request, slug):
    if request.method=="POST":
        form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        if form.is_valid():
            f=form.save(commit=False)
            f.post=post
            f.save()
        return HttpResponseRedirect(f"/posts/{slug}")
    else:
        form=CommentForm()
        post = get_object_or_404(Post, slug=slug)
        tags= post.tags.all()
        comments=Comment.objects.filter(post__slug=slug).order_by("-date")
        context={"post":post,"tags":tags,"comments":comments,"form":form}
        return render(request, "blog/post_detail.html", context)

class PostDetailView(View):
    def get(self,request):
        form=CommentForm()
        post = get_object_or_404(Post, slug=slug)
        # post = next(x for x in all_posts if x.slug == slug)
        tags= post.tags.all()
        comments=Comment.objects.filter(post__slug=slug)
        context={"post":post,"tags":tags,"comments":comments,"form":form}
        return render(request, "blog/post_detail.html", context)
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            slug=self.kwargs['slug']
            context["slug"] = slug
            return context
        
        
    def post(self,request):
        form=CommentForm(request.POST.get('comment'))
        print(form,form.is_valid())
        if form.is_valid():
            all_posts=Post.objects.all()
            post=self.object
            p = next(x for x in all_posts if x.slug == post.slug)
            c=Comment(Comment=request.POST.get('comment'),post=p)
            print(p,c,"heuuu")
            c.save()
            return HttpResponseRedirect(reverse("posts"))
