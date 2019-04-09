from django import forms
from . import models
from .models import Books

class CreateBook(forms.ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'subject', 'price', ]
        