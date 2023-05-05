from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from apps.products.models import Product
from apps.products.serializers import ProductSerializer


class ProductApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
