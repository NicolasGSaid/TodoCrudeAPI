
#  Importa módulos para manipulação de caminhos de arquivos e variáveis de ambiente.

from pathlib import Path 
import os


# BASE_DIR define o diretório raiz do projeto, ou seja, onde o projeto Django está armazenado.

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# MEDIA_URL e MEDIA_ROOT definem onde os arquivos de mídia (uploads de imagens, documentos, etc.) serão armazenados.

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Chave secreta usada pelo Django para criptografia e segurança 

SECRET_KEY = 'vls492jmk+xq5#9mu(dh&dqb%q9x-vv#t535*f$j^8ju54$)c$'

# Quando DEBUG = True, erros são exibidos no navegador. Em produção, deve ser False.

DEBUG = True

# Define quais domínios podem acessar a API. Se estiver vazio ([]), apenas localhost pode acessar

ALLOWED_HOSTS = []


# Lista de apps intalados no django 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders', #Permite CRORS para requisicoes de front end
    'UsuarioApp.apps.UsuarioappConfig', #aplicação personalizada do projeto
    'rest_framework', #Framework para criação de API restfull com Django
]

#Habilita o CORS para todas as origens

CORS_ORIGIN_ALLOW_ALL = True


#São funções que processam as requisiçoes antes de chegarem as views

MIDDLEWARE = [ 
    'corsheaders.middleware.CorsMiddleware', #gerencia o CORS
    'django.middleware.security.SecurityMiddleware', # Reforça a segurança contra ataques como XSS e clickjacking
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', #Protege contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', #Gerencia a autenticação do usuário
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Define qual arquivo contém a configuração de rotas (urls.py).

ROOT_URLCONF = 'DjangoAPI.urls'

# Define como o Django renderiza templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True, #Permite que templates sejam criados a partir de cada app 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configura o Django para rodar em servidores WSGI como o Gunicorn

WSGI_APPLICATION = 'DjangoAPI.wsgi.application'

# Denine o banco de dados que será utilizado

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # SQLITE é o banco padrão, pode ser alterado para outros como MySQL, PostgreSQL, etc.
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Valida as senhas dos usuários, exigindo criterios como tamanho mínimo, caracteres especiais, etc

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configura idioma e fuso Horario

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Define a URL para arquivos estáticos (CSS, JavaScript, imagens, etc.)

STATIC_URL = '/static/'