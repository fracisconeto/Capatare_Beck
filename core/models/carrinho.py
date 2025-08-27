from django.db import models
from .usuario import Usuario
from .produto import Produto

class Carrinho(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="carrinho")
    produtos = models.ManyToManyField(Produto, through="CarrinhoItem")

    def __str__(self):
        return f"Carrinho de {self.usuario}"

class CarrinhoItem(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
