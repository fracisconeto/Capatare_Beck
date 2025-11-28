from rest_framework import serializers
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

        # Comparando a senha diretamente (sem hash)
        if usuario.senha != senha:
            raise serializers.ValidationError("Senha incorreta")

        attrs["usuario"] = usuario
        return attrs
