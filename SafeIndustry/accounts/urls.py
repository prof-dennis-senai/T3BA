from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.accounts_login, name='accounts_login'),
    path('register/', views.accounts_register, name='accounts_register'),
    path('logout/', views.accounts_logout, name='accounts_logout'),
]