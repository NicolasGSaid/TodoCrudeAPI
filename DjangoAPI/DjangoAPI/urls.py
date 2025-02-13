
from django.contrib import admin #Painel de admministração do django 
from django.urls import path #Função para criar rotas

from django.conf.urls import url,include #Permite usar regex e include para incluir arquivos de rotas de outras aplicações
from UsuarioApp import views # Importa as views do app UsuarioApp

urlpatterns = [
    path('admin/', admin.site.urls), # Rota para o painel de administração
    path('', views.home, name='home'), #Rota para a view Home
    path('', include('UsuarioApp.urls')), # Rota para a aplicação personalizada, qualquer requisição será direcionada para esse arquivo de URLs.
]


