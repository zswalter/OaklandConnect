from django.urls import path
from . import views

urlpatterns = [
    path('books/new', views.book_new, name='book_new'),
    path('', views.book_list, name='book_list'),
]