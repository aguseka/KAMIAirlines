from django.urls import path
from . views import create_planes, all_planes

urlpatterns = [
    path('create_planes/', create_planes, name='create_planes'),
    path('all_planes/', all_planes , name='all_planes'),
]
