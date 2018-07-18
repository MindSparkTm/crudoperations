from . import models
from . import serializers
from rest_framework import viewsets, permissions, filters




class Registerusersviewset(viewsets.ModelViewSet):
    """ViewSet for the patientVisit class"""

    queryset = models.Register.objects.all()
    serializer_class = serializers.useradserializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('id','name')











