from django.db import models

class Client(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=20, blank=True, null=True)
