# Importa a classe AppConfig, que é usada para configurar apps dentro do Django.

from django.apps import AppConfig


class UsuarioappConfig(AppConfig): #  Cria uma classe de configuração para o app UsuarioApp, herdando de AppConfig.
    name = 'UsuarioApp' #  Define o nome do aplicativo, que deve corresponder ao nome da pasta do app.
