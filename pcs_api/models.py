from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=32)
    post = models.CharField(max_length=32)
    cpu = models.CharField(max_length=32)
    gpu = models.CharField(max_length=32)
    mobo = models.CharField(max_length=32)
    ram = models.CharField(max_length=32)
    psu = models.CharField(max_length=32)
    cooler = models.CharField(max_length=32)
    storage = models.CharField(max_length=32)
    case = models.CharField(max_length=32)
