

from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Book(models.Model):
    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=13)
    price = models.CharField(max_length=3)
    condition = models.CharField(max_length=30)


class Thread(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')


class Posts(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='post_ID')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_ID')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')