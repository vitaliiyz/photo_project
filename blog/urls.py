from django.urls import path
from blog.views import NewPost, PostsView, SinglePost

urlpatterns = [
    path("create/", NewPost.as_view(), name="new_post_page"),
    path("", PostsView.as_view(), name="blogs_page"),
    path("post/<slug:slug>/", SinglePost.as_view(), name="single_post_page")
]
