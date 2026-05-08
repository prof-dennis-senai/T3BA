from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('criar_empresa/', views.criar_empresa, name='criar_empresa'),
]