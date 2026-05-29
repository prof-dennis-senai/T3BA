from django.db import models

# Create your models here.
class EmpresaModel(models.Model):
    class TipoEmpresa(models.TextChoices):
        PROPRIA = 'P', 'Propria'
        TERCEIRA = 'T', 'Terceira'

    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    tipo_empresa = models.CharField(max_length=1, choices=TipoEmpresa.choices, default=TipoEmpresa.PROPRIA)

    @property
    def cnpj_formatado(self):
        return f"{self.cnpj[:2]}.{self.cnpj[2:5]}.{self.cnpj[5:8]}/{self.cnpj[8:12]}-{self.cnpj[12:14]}"
    
class ColaboradorModel(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    empresa = models.ForeignKey(EmpresaModel, on_delete=models.PROTECT)