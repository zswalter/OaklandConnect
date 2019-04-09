from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Books(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
