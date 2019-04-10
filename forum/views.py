from django.shortcuts import render
from .models import Post
from .forms import CreatePost, CreateComment
from django.utils import timezone
from django.views import generic
from .forms import CreatePost, CreateComment
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from .models import Comment
# Create your views here.
def forum_list(request):
    posts = Post.objects.filter(published_date__lt=timezone.now()).order_by('-published_date')
    comments = Comment.objects.filter(created_on__lte=timezone.now()).order_by('created_on')
    return render(request, 'forum.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('forum_list')
    else:
        form = CreatePost()
        return render(request, 'postForm.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
        return redirect('forum_list')
    else:
        return redirect('forum_list')

def post_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.author = request.user
            comments.created_on = timezone.now()
            comments.post = post
            comments.save()
            return redirect('forum_list')
    else:
        form = CreateComment()
    return render(request, 'commentForm.html', {'form': form})

def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user == comment.author:
        comment.delete()
        return redirect('forum_list')
    else:
        return redirect('forum_list')
