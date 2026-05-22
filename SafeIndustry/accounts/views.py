from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
def accounts_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('listar_empresas')
            else:
                return render(request, 'accounts/pages/login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'accounts/pages/login.html')

def accounts_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('listar_empresas')
        
    return render(request, 'accounts/pages/register.html')

def accounts_logout(request):
    logout(request)
    return redirect('accounts_login')