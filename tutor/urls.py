from django.urls import path
from . import views

urlpatterns = [
    path('tutor/new', views.tutor_new, name='tutor_new'),
    path('', views.tutor_list, name='tutor_list'),
    path('tutor/<int:pk>/edit/', views.tutor_edit, name='tutor_edit'),
    path('tutor/<int:pk>/delete/', views.tutor_delete, name='tutor_delete'),
]