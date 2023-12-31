from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlaneSerializer
from drf_yasg.utils import swagger_auto_schema
from . models import Plane


@swagger_auto_schema(
    methods=['post'],
    request_body=PlaneSerializer(many=True),
    responses={200: PlaneSerializer(many=True)}
)
@api_view(['POST'])
def create_planes(request)-> Response :
    """
    This view is to create a single plane or multiple planes which is maximum 10 planes per batch
    """
    if request.method == 'POST':
        data = request.data

        # Check if 'planes' key is present for bulk creation
        if 'planes' in data and isinstance(data['planes'], list):
            # Limit bulk creation to 10 planes
            if len(data['planes']) > 10:
                return Response({"error": "Bulk creation is limited to 10 planes at a time."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = PlaneSerializer(data=data['planes'], many=True)
        else:
            serializer = PlaneSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_planes(request) -> Response :
    """ 
    Get all available planes
    """
    if request.method == 'GET':
        planes = Plane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def single_plane(request,id) -> Response:
    """
    calling a single plane based on its id in database
    """
    if request.method == 'GET':    
        try:
            plane = Plane.objects.get(pk=id)
        except Plane.DoesNotExist:
            return Response({'error': 'Plane not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PlaneSerializer(plane)
        return Response(serializer.data, status=status.HTTP_200_OK)

