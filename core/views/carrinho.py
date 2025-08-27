from rest_framework import viewsets
from ..models import Carrinho, CarrinhoItem
from ..serializers import CarrinhoSerializer, CarrinhoItemSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

class CarrinhoItemViewSet(viewsets.ModelViewSet):
    queryset = CarrinhoItem.objects.all()
    serializer_class = CarrinhoItemSerializer
