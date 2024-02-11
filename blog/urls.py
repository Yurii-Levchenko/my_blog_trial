from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostsRestView)
router.register('authors', views.AuthorRestView)
router.register('tags', views.TagsRestView)
router.register('comments', views.CommentsRestView)

urlpatterns = [
    path('', views.StartingPageView.as_view(), name="starting-page"),
    path('posts', views.AllPostsView.as_view(), name="posts-page"),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name="post-detail-page"),
    path('read-later', views.ReadLaterView.as_view(), name="read-later"),
    path('rest/', include(router.urls)),
]
