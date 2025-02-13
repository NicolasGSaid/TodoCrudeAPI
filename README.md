# TodoCrudeAPI

API para aplicação TODO List.

## Requisitos (API e UI)

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (recomendado)
- Django 3.1
- NodeJS 12.18.2
- SQLiteStudio

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

