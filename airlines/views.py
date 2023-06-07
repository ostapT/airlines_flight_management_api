from rest_framework import viewsets

from airlines.models import Plane
from airlines.serializers import PlaneSerializer, PlaneDetailSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PlaneDetailSerializer

        return self.serializer_class
