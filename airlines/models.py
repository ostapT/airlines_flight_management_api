import math

from django.db import models


class Plane(models.Model):
    model_name = models.CharField(max_length=63)
    plane_id = models.PositiveIntegerField(unique=True)
    passengers = models.PositiveIntegerField()

    @property
    def fuel_consumption(self) -> float:
        fuel_consumption = math.log(self.plane_id) * 0.80
        fuel_consumption += self.passengers * 0.002
        return round(fuel_consumption, 2)

    @property
    def max_flight_duration(self) -> float:
        fuel_tank_capacity = self.plane_id * 200
        fuel_consumption = self.fuel_consumption

        flight_duration_minutes = fuel_tank_capacity / fuel_consumption

        return round(flight_duration_minutes, 2)

    def __str__(self) -> str:
        return self.model_name
