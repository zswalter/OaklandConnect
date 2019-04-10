from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Tutors(models.Model):
    TIME_CHOICES = [
        ('1:00', '1AM'),
        ('2:00', '2AM'),
        ('3:00', '3AM'),
        ('4:00', '4AM'),
        ('5:00', '5AM'),
        ('6:00', '6AM'),
        ('7:00', '7AM'),
        ('8:00', '8AM'),
        ('9:00', '9AM'),
        ('10:00', '10AM'),
        ('11:00', '11AM'),
        ('12:00', '12PM'),
        ('13:00', '1PM'),
        ('14:00', '2PM'),
        ('15:00', '3PM'),
        ('16:00', '4PM'),
        ('17:00', '5PM'),
        ('18:00', '6PM'),
        ('19:00', '7PM'),
        ('20:00', '8PM'),
        ('21:00', '9PM'),
        ('22:00', '10PM'),
        ('23:00', '11PM'),
        ('24:00', '12AM'),

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
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user


