#Módulo nativo do python usado para manipular as variavéis de ambiente

import os 

#Módulo nativo do python usado para manipular as variavéis de ambiente

from django.core.asgi import get_asgi_application 


#Define a variável de ambiente DJANGO_SETTINGS_MODULE apontando para o settings.py do projeto.
#O django usa essa variavel para saber onde buscar as configurações do projeto

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoAPI.settings') 


                                                                       
#Cria uma instancia da aplicação ASGI
#Essa variavel sera usada pelo servidor ASGI para rodar o servidor de forma assincrona
#O servidor ASGI é responsavel por gerenciar as conexões com o servidor e as requisições HTTP

application = get_asgi_application()

