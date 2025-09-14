from django.db import models
from vehicles.models import Vehicle
from services.models import Service
from spareparts.models import SparePart

class Turn(models.Model):
    STATES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("FINISHED", "Finished"),
        ("CANCELED", "Canceled")
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='turns')
    date = models.DateField()
    hour = models.TimeField()
    state = models.CharField(max_length=10, choices=STATES, default="PENDING")
    description = models.TextField(blank=True, null=True)
    
    # Relations with services and spare parts
    services = models.ManyToManyField(Service, blank=True, related_name='turns')
    spareparts = models.ManyToManyField(SparePart, blank=True, related_name='turns')
    
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Turn {self.date} at {self.hour} - {self.vehicle}'


