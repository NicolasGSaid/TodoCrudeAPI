from django.urls import path #funçao para definir view associada a uma url
from UsuarioApp import views #importa as views do app UsuarioApp

from django.conf.urls.static import static #importa a função static para servir arquivos de mídia
from django.conf import settings #importa as configurações do projeto

urlpatterns = [

    path('tarefa/', views.tarefaApi),
    path('tarefa/<int:id>', views.tarefaApi),
]
       