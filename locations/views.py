from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer


class LocationModelViewset(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
