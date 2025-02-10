# Importa o módulo models do Django, que permite definir modelos de banco de dados usando classes Python.

from django.db import models


# Define a classe Tarefas que representa uma tabela de banco de dados chamada Tarefas.
# Ela herda de models.Model, o que significa que o django tratará essa classe como um modelo de banco de dados.

class Tarefas(models.Model):
    
    TarefaId = models.AutoField(primary_key=True) # campo númerico que se auto incrementa, definido como chave primária da tabela
    TarefaNome = models.CharField(max_length=100) # campo de texto com no máximo 100 caracteres
    TarefaDescricao = models.CharField(max_length=1000, default="Sem descrição") # campo de texto com no máximo 1000 caracteres
    TarefaConcluida = models.BooleanField(default=False) # campo booleano que indica se a tarefa foi concluída ou não
