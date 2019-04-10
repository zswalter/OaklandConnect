from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Tutors(models.Model):
    TIME_CHOICES = [
        ('Not Available', 'Not Available'),
        ('1:00 AM', '1:00 AM'),
        ('2:00 AM', '2:00 AM'),
        ('3:00 AM', '3:00 AM'),
        ('4:00 AM', '4:00 AM'),
        ('5:00 AM', '5:00 AM'),
        ('6:00 AM', '6:00 AM'),
        ('7:00 AM', '7:00 AM'),
        ('8:00 AM', '8:00 AM'),
        ('9:00 AM', '9:00 AM'),
        ('10:00 AM', '10:00 AM'),
        ('11:00 AM', '11:00 AM'),
        ('12:00 PM', '12:00 PM'),
        ('1:00 PM', '1:00 PM'),
        ('2:00 PM', '2:00 PM'),
        ('3:00 PM', '3:00 PM'),
        ('4:00 PM', '4:00 PM'),
        ('5:00 PM', '5:00 PM'),
        ('6:00 PM', '6:00 PM'),
        ('7:00 PM', '7:00 PM'),
        ('8:00 PM', '8:00 PM'),
        ('9:00 PM', '9:00 PM'),
        ('10:00 PM', '10:00 PM'),
        ('11:00 PM', '11:00 PM'),
        ('12:00 AM', '12:00 AM'),

    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mon_start = models.CharField(max_length=200, choices=TIME_CHOICES)
    mon_end = models.CharField(max_length=200, choices=TIME_CHOICES)
    tue_start = models.CharField(max_length=200, choices=TIME_CHOICES)
    tue_end = models.CharField(max_length=200, choices=TIME_CHOICES)
    wed_start = models.CharField(max_length=200,choices=TIME_CHOICES)
    wed_end = models.CharField(max_length=200, choices=TIME_CHOICES)
    thur_start = models.CharField(max_length=200, choices=TIME_CHOICES)
    thur_end = models.CharField(max_length=200, choices=TIME_CHOICES)
    fri_start = models.CharField(max_length=200, choices=TIME_CHOICES)
    fri_end = models.CharField(max_length=200, choices=TIME_CHOICES)
    subject = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user


