from django.db import models
from .pedido import Pedido
from .produto import Produto

class Iten(models.Model):  # pode ser melhor "ItemPedido"
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
