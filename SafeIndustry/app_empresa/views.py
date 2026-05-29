from django.shortcuts import render, redirect
from app_empresa.models import EmpresaModel, ColaboradorModel
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
@permission_required('app_empresa.view_empresamodel', raise_exception=True)
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

@login_required
@permission_required('app_empresa.add_empresamodel', raise_exception=True)
def criar_empresa(request):
    nome, cnpj, email, telefone = '', '', '', ''

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if nome and cnpj and email and telefone:
            empresa = EmpresaModel(
                nome=nome,
                cnpj=cnpj,
                email=email,
                telefone=telefone
            )
            empresa.save()

            return redirect('listar_empresas')
        
    return render(request, 'app_empresa/pages/criar_empresa.html', {
        'nome': nome,
        'cnpj': cnpj,
        'email': email,
        'telefone': telefone
    })

@login_required
@permission_required('app_empresa.delete_empresamodel', raise_exception=True)
def remover_empresa(request, id):
    empresa = EmpresaModel.objects.get(id=id)
    empresa.delete()

    return redirect('listar_empresas')

@login_required
@permission_required('app_empresa.change_empresamodel', raise_exception=True)
def atualizar_empresa(request, id):
    empresa = EmpresaModel.objects.get(id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if nome and cnpj and email and telefone:
            empresa.nome = nome
            empresa.cnpj = cnpj
            empresa.email = email
            empresa.telefone = telefone
            empresa.save()

            return redirect('listar_empresas')
        
    return render(request, 'app_empresa/pages/atualizar_empresa.html', {'empresa': empresa})


# Colaboradores

@login_required
@permission_required('app_empresa.view_colaboradormodel', raise_exception=True)
def listar_colaboradores(request):
    colaboradores = ColaboradorModel.objects.all()

    return render(
        request,
        'app_empresa/pages/listar_colaboradores.html',
        {'colaboradores': colaboradores}
    )


@login_required
@permission_required('app_empresa.add_colaboradormodel', raise_exception=True)
def criar_colaborador(request):
    empresas = EmpresaModel.objects.all()

    nome, email, telefone = '', '', ''
    empresa_id = ''

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        empresa_id = request.POST.get('empresa')

        if nome and email and telefone and empresa_id:
            empresa = EmpresaModel.objects.get(id=empresa_id)

            colaborador = ColaboradorModel(
                nome=nome,
                email=email,
                telefone=telefone,
                empresa=empresa
            )

            colaborador.save()

            return redirect('listar_colaborador')

    return render(
        request,
        'app_empresa/pages/criar_colaborador.html',
        {
            'empresas': empresas,
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'empresa_id': empresa_id
        }
    )


@login_required
@permission_required('app_empresa.delete_colaboradormodel', raise_exception=True)
def remover_colaborador(request, id):
    colaborador = ColaboradorModel.objects.get(id=id)
    colaborador.delete()

    return redirect('listar_colaborador')


@login_required
@permission_required('app_empresa.change_colaboradormodel', raise_exception=True)
def atualizar_colaborador(request, id):
    colaborador = ColaboradorModel.objects.get(id=id)
    empresas = EmpresaModel.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        empresa_id = request.POST.get('empresa')

        if nome and email and telefone and empresa_id:
            empresa = EmpresaModel.objects.get(id=empresa_id)

            colaborador.nome = nome
            colaborador.email = email
            colaborador.telefone = telefone
            colaborador.empresa = empresa

            colaborador.save()

            return redirect('listar_colaborador')

    return render(
        request,
        'app_empresa/pages/atualizar_colaborador.html',
        {
            'colaborador': colaborador,
            'empresas': empresas
        }
    )