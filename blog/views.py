# for returning corresponding rendered html pages
from django.shortcuts import render, get_object_or_404
from .models import Author, Post, Tag


def get_date(post):
    return post['date']
    # or return post.get('date')


# Create your views here.


def starting_page(request):
    # sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = Post.objects.order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all_posts.html", {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
