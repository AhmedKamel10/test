from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse

# Create your models here.

class mode(models.Model):
    name = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name
class username(models.Model):
    username= models.CharField(max_length=255, blank=True, null=True)
    mode = models.ForeignKey(mode, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username