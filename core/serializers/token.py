from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializador customizado para autenticação via email ao invés de username.
    """

    username_field = 'email'
