from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from . models import Plane

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'
        read_only_fields = ('cons_per_mnt', 'tot_cons_per_minute', 'max_flight_time', 'fuel_cap', 'max_pass_consumption',)
    
    def validate_passenger_capacity(self, value: int ) -> int :
        if value > 500:
            raise serializers.ValidationError("Passenger capacity cannot exceed 500.")
        return value
    
    
    @swagger_auto_schema(
        request_body=Plane,
        responses={200: 'self'}
    )
    def create(self, validated_data: dict):
        return super(PlaneSerializer, self).create(validated_data)