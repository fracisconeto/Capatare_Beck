from rest_framework import viewsets
from ..models import Iten
from ..serializers import ItenSerializer

class ItenViewSet(viewsets.ModelViewSet):
    queryset = Iten.objects.all()
    serializer_class = ItenSerializer
