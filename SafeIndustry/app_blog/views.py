from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app_blog/pages/home.html')

def sobre(request):
    return render(request, 'app_blog/pages/sobre.html')