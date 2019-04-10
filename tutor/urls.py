from django.urls import path
from . import views

urlpatterns = [
    path('tutor/new', views.tutor_new, name='tutor_new'),
    path('', views.tutor_list, name='tutor_list'),
]