from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from django.db.models import Q
from .models import Turn
from .serializers import TurnSerializer 

class TurnViewSet(viewsets.ModelViewSet):
    serializer_class = TurnSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Turn.objects.filter(Q(user=user) | Q(mechanic=user))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def perform_update(self, serializer):
        turn = self.get_object()
        user = self.request.user
        if turn.user != user and turn.mechanic != user:
            raise PermissionDenied("You do not have permission to modify this turn.")
        serializer.save()
        
    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user != user:
            raise PermissionDenied("You do not have permission to delete this turn.")
        instance.delete()
