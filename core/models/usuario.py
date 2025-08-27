from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)  # você pode criptografar depois com hashlib ou bcrypt
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)  # 000.000.000-00
    data_nascimento = models.DateField(blank=True, null=True)
    genero = models.CharField(
        max_length=20,
        choices=[
            ("M", "Masculino"),
            ("F", "Feminino"),
            ("O", "Outro"),
            ("N", "Prefiro não informar"),
        ],
        blank=True,
        null=True
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
