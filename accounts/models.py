from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Student', 'Student'),
        ('Tutor', 'Tutor'),
        ('Professor', 'Professor'),
    )

    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        return self.username
    def is_student(self):
        user = self
        if user.user_type == 'Student':
            return True
        else:
            return False

    def is_tutor(self):
        user = self
        if user.user_type == 'Tutor':
            return True
        else:
            return False

    def is_professor(self):
        user = self
        if user.user_type == 'Professor':
            return True
        else:
            return False

