from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers.login_serializer import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data["usuario"]

        return Response({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "telefone": usuario.telefone,
            "cpf": usuario.cpf,
        }, status=status.HTTP_200_OK)
