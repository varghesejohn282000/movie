from django.db import models


class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')

# Create your models here.
