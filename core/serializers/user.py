from rest_framework.serializers import ModelSerializer

from core.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        depth = 1

    def create(self, validated_data):
        """Cria um novo usuário com a senha criptografada."""
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """Atualiza um usuário, criptografando a senha se fornecida."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
