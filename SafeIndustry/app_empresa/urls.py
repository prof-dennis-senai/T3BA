from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_empresas, name='listar_empresas'),
    path('criar_empresa/', views.criar_empresa, name='criar_empresa'),
    path('remover_empresa/<int:id>', views.remover_empresa, name='remover_empresa'),
    path('atualizar_empresa/<int:id>', views.atualizar_empresa, name='atualizar_empresa'),
]