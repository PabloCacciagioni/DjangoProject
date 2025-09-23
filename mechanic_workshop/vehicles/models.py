from django.db import models
from client.models import Users

class Vehicle(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='vehicles')
    
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    registration = models.CharField(max_length=50, unique=True)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30, blank=True, null=True)
    
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.make} {self.model} ({self.registration})'