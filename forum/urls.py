from django.urls import path
from . import views

urlpatterns = [
    path('forum/new', views.post_new, name='post_new'),
    path('', views.forum_list, name='forum_list'),
]