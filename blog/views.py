from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, ListView
from django.views.generic.detail import DetailView

from blog.forms import PostForm
from blog.models import Post, Tag


def new_post(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden(content="Permission denied")
    context = {"post_form": PostForm(), "page_tag": "post"}
    if request.method == "POST":
        user_data = request.POST.copy()
        user_data["author"] = request.user
        form = PostForm(user_data, request.FILES)
        if form.is_valid():
            form.save()
            redirect("home_page")
        context["post_form"] = form
    return render(request, "new_post.html", context)


class NewPost(FormView):
    template_name = "new_post.html"
    form_class = PostForm

    def get_form_kwargs(self):
        kwargs = {"initial": self.get_initial(), "prefix": self.get_prefix()}

        if self.request.method in ("POST", "PUT"):
            user_data = self.request.POST.copy()
            user_data["author"] = self.request.user
            kwargs.update({"data": user_data, "files": self.request.FILES})
        return kwargs

    def get_success_url(self):
        return self.request.GET.get("next", reverse("home_page"))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostsView(ListView):
    template_name = "posts.html"
    model = Post
    paginate_by = 1

    def get_queryset(self):
        tag_name = self.request.GET.get("tag", default=None)
        if tag_name is not None:
            return Tag.objects.get(value=tag_name).posts.all()
        return super().get_queryset()


class SinglePost(DetailView):
    model = Post
    template_name = "single_post.html"
