from django.db import models

# Create your models here.
class EmpresaModel(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome