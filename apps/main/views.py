from rest_framework.viewsets import ModelViewSet

from apps.main.models import Main
from apps.main.serializers import MainSerializer


class MainApiViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
