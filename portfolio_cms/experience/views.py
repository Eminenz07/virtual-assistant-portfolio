from rest_framework import viewsets
from .models import Experience
from .serializers import ExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filterset_fields = ['is_current']
