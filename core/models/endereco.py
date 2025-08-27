from django.db import models
from .usuario import Usuario

class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="enderecos")
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"
