from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from . models import Plane

class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = '__all__'
        extra_kwargs = {
            'passenger_capacity': {'choices': [(100, '100'), (200, '200'), (300, '300'), (400, '400'), (500, '500')]}
        }
        read_only_fields = ('cons_per_mnt', 'tot_cons_per_minute', 'max_flight_time', 'fuel_cap', 'max_pass_consumption',)
    
    @swagger_auto_schema(
        request_body=Plane,
        responses={200: 'self'}
    )

    def create(self, validated_data):
        return super(PlaneSerializer, self).create(validated_data)

#class BulkPlaneSerializer(serializers.Serializer):
#    planes = PlaneSerializer(many=True)