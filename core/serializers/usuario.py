from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            "senha": {"write_only": True}
        }

    def create(self, validated_data):
        # Criptografa a senha antes de salvar no banco
        validated_data["senha"] = make_password(validated_data["senha"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Se senha for alterada, criptografar de novo
        if "senha" in validated_data:
            validated_data["senha"] = make_password(validated_data["senha"])
        return super().update(instance, validated_data)
