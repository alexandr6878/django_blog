from django.shortcuts import render
from .forms import CreatePostForm
from .models import Post
from django.http import HttpResponseRedirect



def index(request):
    posts=Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "index.html", context)

def create_post(request):
    form = CreatePostForm()
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            comment = Post(
                author=form.cleaned_data["author"],
                tittle=form.cleaned_data["tittle"],
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    context = {
        "form": CreatePostForm(),
    }
    return render(request, "create_post.html", context)