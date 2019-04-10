from django.urls import path
from . import views

urlpatterns = [
    path('forum/new', views.post_new, name='post_new'),
    path('forum/<int:pk>/comment/', views.post_comment, name='post_comment'),
    path('', views.forum_list, name='forum_list'),
    path('forum/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]