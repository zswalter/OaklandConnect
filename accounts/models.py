from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'tutor'),
        (3, 'professor'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username
    def is_student(self):
        user = self
        if user.user_type == 1:
            return True
        else:
            return False

    def is_tutor(self):
        user = self
        if user.user_type == 2:
            return True
        else:
            return False

    def is_professor(self):
        user = self
        if user.user_type == 3:
            return True
        else:
            return False

