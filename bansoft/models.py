from turtle import title
from django.db import models
from django.utils import timezone


# Create your models here.
class Aboutus(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title