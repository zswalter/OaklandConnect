from django.urls import path
from . import views

urlpatterns = [
    path('forum/new', views.post_new, name='post_new'),
    path('forum/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('', views.forum_list, name='forum_list'),
]