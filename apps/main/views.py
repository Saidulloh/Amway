from rest_framework.viewsets import ModelViewSet

from apps.main.models import Main, Consultation
from apps.main.serializers import MainSerializer, ConsultationSerializer


class MainApiViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class ConsultationApiViewSet(ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer
