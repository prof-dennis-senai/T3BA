from django.shortcuts import render

# Create your views here.
def listar_empresas(request):
    return render(request, 'app_empresa/pages/listar_empresas.html')