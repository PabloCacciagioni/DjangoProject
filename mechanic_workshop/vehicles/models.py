from django.db import models
from django.conf import settings

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicles')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)
    plate = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=50)
    delivery_date = models.DateField()
    
    class Meta:
        ordering = ['-delivery_date']
        
    def __str__(self):
        return f"{self.brand} {self.model} ({self.plate})"