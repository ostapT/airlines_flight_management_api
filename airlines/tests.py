
import unittest
from django.test import TestCase
from rest_framework.test import APIClient

from airlines.serializers import PlaneDetailSerializer
from .models import Plane


class PlaneTestCase(TestCase):

    def test_fuel_consumption(self):
        plane = Plane.objects.create(model_name="Test Plane", plane_id=4, passengers=100)
        fuel_consumption = plane.fuel_consumption

        self.assertEqual(fuel_consumption, 1.31)

    def test_max_flight_duration(self):
        plane = Plane(model_name="Test Plane", plane_id=4, passengers=100)
        max_flight_duration = plane.max_flight_duration

        self.assertEqual(max_flight_duration, 610.69)


class PlaneViewSetTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.plane = Plane.objects.create(model_name="Test Plane", plane_id=4, passengers=100)

    def test_retrieve_plane_detail(self):
        url = f"/api/airlines/{self.plane.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        expected_data = PlaneDetailSerializer(self.plane).data
        self.assertEqual(response.data, expected_data)


if __name__ == '__main__':
    unittest.main()
