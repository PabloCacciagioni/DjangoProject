from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Vehicle
from .serializers import VehicleSerializer

# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Vehicle.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def perform_update(self, serializer):
        vehicle = self.get_object()
        if vehicle.owner != self.request.user:
            raise PermissionDenied("You do not have permission to edit this vehicle.")
        serializer.save()
        
    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permission to delete this vehicle.")
        instance.delete()
