from django.conf.urls import url #funçao para definir view associada a uma url
from UsuarioApp import views #importa as views do app UsuarioApp

from django.conf.urls.static import static #importa a função static para servir arquivos de mídia
from django.conf import settings #importa as configurações do projeto

urlpatterns = [

    url(r'^tarefa/$',views.tarefaApi),
    url(r'^tarefa/([0-9]+)$',views.tarefaApi),
       
] 