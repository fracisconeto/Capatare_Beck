from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from core.models import Usuario

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        senha = attrs.get("senha")

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado")

        # Verifica senha usando hash
        if not check_password(senha, usuario.senha):
            raise serializers.ValidationError("Senha incorreta")

        attrs["usuario"] = usuario
        return attrs
