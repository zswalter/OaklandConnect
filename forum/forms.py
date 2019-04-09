from django import forms
from . import models
from .models import Post, Comment

class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body',]

class CreateComment(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body', ]
