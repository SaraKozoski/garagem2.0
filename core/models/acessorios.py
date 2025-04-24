#primeira tabela
from django.db import models

class Acessorios(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.id}) {self.descricao}  "
#NAO ESQUECE DE POR NA PAGINA _INIT__.PY
#terminal(pdm run migrate)
