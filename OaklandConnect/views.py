from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Book


def home(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})