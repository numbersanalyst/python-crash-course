from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import BlogPostForm
from .models import BlogPost


def index(request):
    """Render the index page for the blog app."""
    blogs = BlogPost.objects.order_by("-date_added")
    context = {"blogs": blogs}
    return render(request, "blogs/index.html", context)


@login_required
def new_post(request):
    """Add a new blog post."""
    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"form": form}
    return render(request, "blogs/new_post.html", context)


@login_required
def edit_post(request, blog_id):
    """Edit an existing blog post."""
    blog = BlogPost.objects.get(id=blog_id)

    if blog.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blogs:index")

    context = {"form": form, "blog": blog}
    return render(request, "blogs/edit_post.html", context)
