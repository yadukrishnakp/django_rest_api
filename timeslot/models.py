from django.db import models


# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100, blank=True),
    time_from = models.TimeField(blank=False)
    time_to = models.TimeField(blank=False)

