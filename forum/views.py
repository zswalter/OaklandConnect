from django.shortcuts import render
from .models import Post
from .forms import CreatePost
from django.utils import timezone
from django.views import generic
from .forms import CreatePost
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.
def forum_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
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
