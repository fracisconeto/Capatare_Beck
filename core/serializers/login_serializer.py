from rest_framework import serializers
from django.contrib.auth import authenticate
from core.models import User  # ajuste para o seu AUTH_USER_MODEL

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # autentica usando email como username
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Credenciais inválidas.")

        if not user.is_active:
            raise serializers.ValidationError("Usuário inativo.")

        attrs["usuario"] = user
        return attrs
