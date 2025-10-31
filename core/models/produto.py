from django.db import models
from .categoria import Categoria

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(
    Categoria,
    on_delete=models.SET_NULL,
    related_name="produtos",
    null=True,
    blank=True,
    default=None,
    )

    image1=models.CharField(max_length=255)
    image2=models.CharField(max_length=255)

    def __str__(self):
        return self.nome
