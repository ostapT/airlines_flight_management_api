from django.urls import path, include
from rest_framework import routers

from airlines.views import PlaneViewSet

router = routers.DefaultRouter()
router.register("airlines", PlaneViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airlines"
