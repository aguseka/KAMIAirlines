

from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Plane
from math import log
from config.configs import TANK, PASS_CONSUMPTION, FUEL_CONS


class CreatePlanesAPITest(APITestCase):
    def test_create_single_plane(self) -> None:
        data = {
            "planes": [
                {
                    "plane_name": "A 320-300",
                    "id_by_user": 5,
                    "passenger_capacity": 300
                }
            ]
        }

        response = self.client.post('/api/create_planes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plane.objects.count(), 1)

        # Retrieve the created plane
        created_plane = Plane.objects.get(plane_name="A 320-300")

        # Add assertions for calculated fields
        self.assertAlmostEqual(created_plane.fuel_cap, 5 * TANK)
        self.assertAlmostEqual(created_plane.cons_per_mnt, log(5) * FUEL_CONS)
        self.assertAlmostEqual(created_plane.max_pass_consumption, 300 * PASS_CONSUMPTION)
        self.assertAlmostEqual(created_plane.tot_cons_per_minute, created_plane.cons_per_mnt + created_plane.max_pass_consumption)
        self.assertAlmostEqual(created_plane.max_flight_time, created_plane.fuel_cap / created_plane.tot_cons_per_minute)

    def test_bad_request(self) -> None:
        data = {
            "plan": [
                {
                    "plane_name": "A 320-300",
                    "id_by_user": 5,
                    "passenger_capacity": 300
                }
            ]
        }

        response = self.client.post('/api/create_planes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Plane.objects.count(), 0)


    def test_create_multiple_planes(self) -> None:
        data = {
            "planes": [
                {
                    "plane_name": f"A 320-{i}",
                    "id_by_user": 5,
                    "passenger_capacity": 300
                } for i in range(1, 11)
            ]
        }

        response = self.client.post('/api/create_planes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plane.objects.count(), 10)
        

    def test_create_too_many_planes(self) -> None :
        data = {
            "planes": [
                {
                    "plane_name": f"A 320-{i}",
                    "id_by_user": 5,
                    "passenger_capacity": 300
                } for i in range(1, 13)
            ]
        }

        response = self.client.post('/api/create_planes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Bulk creation is limited to 10 planes at a time.", str(response.data))
        self.assertEqual(Plane.objects.count(), 0)

class GetAllPlanesAPITest(APITestCase):
    def setUp(self)-> None :
        # Create some planes for testing
        Plane.objects.create(plane_name='Test Plane 1', id_by_user=1, passenger_capacity=200)
        Plane.objects.create(plane_name='Test Plane 2', id_by_user=2, passenger_capacity=300)

    def test_get_all_planes(self) -> None:
        response = self.client.get('/api/all_planes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['plane_name'], 'Test Plane 1')
        self.assertEqual(response.data[1]['plane_name'], 'Test Plane 2')

class GetSinglePlaneAPITest(APITestCase):
    def setUp(self):
        # Create a sample plane for testing
        self.sample_plane = Plane.objects.create(
            plane_name='Sample Plane',
            id_by_user=1,
            passenger_capacity=200,
        )
        self.client = APIClient()

    def test_get_single_plane(self):
        response = self.client.get(f'/api/single_plane/{self.sample_plane.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['plane_name'], 'Sample Plane')

    def test_non_exist_plane(self):
        response = self.client.get('/api/single_plane/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# Testing the modified serializer
class PlaneSerializerTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_passenger_capacity_validation(self):
        # Attempt to create a plane with invalid passenger capacity (more than 500)
        invalid_data = {
            "plane_name": "Test Plane",
            "id_by_user": 1,
            "passenger_capacity": 600,  # Exceeding the limit
        }

        response = self.client.post('/api/create_planes/', data=invalid_data, format='json')

        # Assert that the request returns a 400 Bad Request status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Assert that the response contains the validation error message
        self.assertIn("Passenger capacity cannot exceed 500.", str(response.data))

    def test_passenger_capacity_validation_successful(self):
        # Attempt to create a plane with valid passenger capacity
        valid_data = {
            "plane_name": "Test Plane",
            "id_by_user": 1,
            "passenger_capacity": 400,  # Within the limit
        }

        response = self.client.post('/api/create_planes/', data=valid_data, format='json')

        # Assert that the request is successful (201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
