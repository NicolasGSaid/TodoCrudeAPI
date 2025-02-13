# TodoCrudeAPI

API para aplicação TODO List.

## Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)

## Instalação

Siga os passos abaixo para configurar e executar a API localmente na sua máquina:

1. Clone o repositório:

    ```bash
    git clone https://github.com/NicolasGSaid/TodoCrudeAPI.git
    cd TodoCrudeAPI
    ```

2. Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor:

    ```bash
    python manage.py runserver
    ```

## Solução de Problemas

### ImportError: cannot import name 'url' from 'django.conf.urls'

Esse erro ocorre devido a mudanças na forma como as URLs são importadas no Django. Para resolver esse problema, você pode precisar atualizar seu código para usar `from django.urls import path`.

Verifique se o arquivo `urls.py` está assim:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Adicione suas outras URLs aqui
]
