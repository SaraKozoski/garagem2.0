#quarta tabela
from django.db import models

from .acessorios import Acessorios
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorios, blank=True)

    def __str__(self):
        return f"ID {self.id} - {self.modelo} - {self.cor} - {self.ano}"
