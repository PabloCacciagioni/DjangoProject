from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'owner', 'brand', 'model', 'year', 'vin', 'plate', 'color', 'delivery_date']
        read_only_fields = ['id', 'owner']
        