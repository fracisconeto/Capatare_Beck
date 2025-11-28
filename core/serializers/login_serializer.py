from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email e senha são obrigatórios.")

        # Seu USERNAME_FIELD é 'email', então usamos username=email
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("Credenciais inválidas.")

        if not user.is_active:
            raise serializers.ValidationError("Usuário inativo.")

        attrs["usuario"] = user
        return attrs
