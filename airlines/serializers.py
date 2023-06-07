from rest_framework import serializers

from airlines.models import Plane


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ("id", "plane_id", "model_name", "passengers")


class PlaneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = (
            "id",
            "plane_id",
            "model_name",
            "passengers",
            "fuel_consumption",
            "max_flight_duration",
        )
