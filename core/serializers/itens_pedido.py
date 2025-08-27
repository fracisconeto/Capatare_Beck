from rest_framework import serializers
from ..models import Iten

class ItenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iten
        fields = '__all__'  # pedido e produto como IDs
