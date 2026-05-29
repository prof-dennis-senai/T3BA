from django.urls import path
from . import views

urlpatterns = [
    # Empresas
    path('', views.listar_empresas, name='listar_empresas'),
    path('criar_empresa/', views.criar_empresa, name='criar_empresa'),
    path('remover_empresa/<int:id>', views.remover_empresa, name='remover_empresa'),
    path('atualizar_empresa/<int:id>', views.atualizar_empresa, name='atualizar_empresa'),

    # Colaboradores
    path('listar_colaboradores/', views.listar_colaboradores, name='listar_colaborador'),
    path('criar_colaborador/', views.criar_colaborador, name='criar_colaborador'),
    path('remover_colaborador/<int:id>', views.remover_colaborador, name='remover_colaborador'),
    path('atualizar_colaborador/<int:id>', views.atualizar_colaborador, name='atualizar_colaborador'),
]