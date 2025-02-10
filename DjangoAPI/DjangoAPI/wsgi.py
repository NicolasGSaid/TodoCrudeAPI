#Módulo nativo do python usado para manipular as variavéis de ambiente
import os 

# Importa a função que cria a aplicação WSGI do Django
from django.core.wsgi import get_wsgi_application 

#Define a variável de ambiente DJANGO_SETTINGS_MODULE apontando para o settings.py do projeto.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAPI.settings')

#Cria uma instancia da aplicação WSGI
application = get_wsgi_application()
