from django.shortcuts import render
from app_empresa.models import EmpresaModel

# Create your views here.
def listar_empresas(request):
    # empresas1 = EmpresaModel(
    #     nome='Luzia e Sônia Transportes Ltda',
    #     cnpj='47568553000109',
    #     email='FqJ4k@example.com',
    #     telefone='(18) 3724-8390'
    # )

    # empresas2 = EmpresaModel(
    #     nome='Otávio e Tânia Locações de Automóveis Ltda',
    #     cnpj='70966594000175',
    #     email='producao@otavioetanialocacoesdeautomoveisltda.com.br',
    #     telefone='(11) 3748-2999'
    # )

    # empresas3 = EmpresaModel(
    #     nome='Almeida montadora Ltda',
    #     cnpj='47568953000109',
    #     email='info@almeidamontadora.com',
    #     telefone='(18) 3724-9631'
    # )

    # empresas4 = EmpresaModel(
    #     nome='Santos e Silva Transportes Ltda',
    #     cnpj='42368553000109',
    #     email='santos@gmail.com',
    #     telefone='(18) 3724-8390'
    # )

    # empresas1.save()
    # empresas2.save()
    # empresas3.save()
    # empresas4.save()

    dados_empresas = EmpresaModel.objects.all()
    
    return render(request, 'app_empresa/pages/listar_empresas.html', {'empresas': dados_empresas})