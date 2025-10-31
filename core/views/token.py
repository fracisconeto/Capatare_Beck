from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers.token import EmailTokenObtainPairSerializer


class EmailTokenObtainPairView(TokenObtainPairView):
    """
    View customizada para obter tokens JWT usando email ao invés de username.
    """

    serializer_class = EmailTokenObtainPairSerializer
