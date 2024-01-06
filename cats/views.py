from rest_framework import viewsets

from cats.models import Cat, Pair
from cats.serializers import CatSerializer, PairSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cats to be viewed or edited.
    """

    queryset = Cat.objects.all().filter()
    serializer_class = CatSerializer


class PairViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cats to be viewed or edited.
    """

    queryset = Pair.objects.all()
    serializer_class = PairSerializer
