from django import forms
from . import models
from .models import Post

class CreatePost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body',]
