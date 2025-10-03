import uuid
from django.db import models
from django.conf import settings
from vehicles.models import Vehicle

class Turn(models.Model):
    class StateChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        CANCELLED = 'CANCELLED', 'Cancelled'
        
    id = models.AutoField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='turns_solicited'
    )
    mechanic = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='turns_assigned'
    )
    
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        related_name='turns'
    )
    
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    
    state = models.CharField(
        max_length=20,
        choices=StateChoices.choices,
        default=StateChoices.PENDING
    )
    
    description_service = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'Turn {self.id} - {self.vehicle} - ({self.state})'
