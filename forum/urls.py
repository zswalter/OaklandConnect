from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_list, name='forum_list')
]