# for returning corresponding rendered html pages
from django.shortcuts import render, get_object_or_404
from .models import Author, Post, Tag


from django.views.generic import DetailView, ListView

def get_date(post):
    return post['date']
    # or return post.get('date')


# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date",]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    

# def starting_page(request):
#     # sorted_posts = sorted(all_posts, key=get_date)
#     latest_posts = Post.objects.order_by('-date')[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts(request):
#     all_posts = Post.objects.all()
#     return render(request, "blog/all_posts.html", {
#         'all_posts': all_posts
#     })


class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        identified_post = self.object
        context["post_tags"] = identified_post.tags.all()
        return context
    

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
    
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })
