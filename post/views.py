from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def posts_list(request):
    posts = Post.objects.filter(owner=request.user)
    post_length = len(posts)
    temp_var = {"allPosts": posts, "post_length" : post_length}
    return render(request, "post/posts_list.html", temp_var)

@login_required
def single_post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/single_post.html", {"post": post, "id" : post_id})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # dont save yet, i want to add user/owner
            post.owner = request.user   # get currently logged in user => request.user
            post.save()
            return redirect('posts_list')
    else:
        form = PostForm()
    
    return render(request, "post/new_post.html", {"form": form})


@login_required
def edit_post(request, post_id):
    
    post = Post.objects.get(id = post_id)
    
    if (request.method == "POST"):
        form = PostForm(request.POST, request.FILES, instance=post)
        if (form.is_valid()):
            form.save()
            return redirect('posts_list')
    else:
        form = PostForm(instance=post) # create an empty form       
    
    return render(request, "post/edit_post.html",  {"post": post})


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id = post_id)
    
    if (request.method == "POST"):
        post.delete()
        
    return redirect('posts_list')
    
    
    
    
