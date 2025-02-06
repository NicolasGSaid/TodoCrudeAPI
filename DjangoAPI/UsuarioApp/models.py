from django.db import models




class Tarefas(models.Model):
    TarefaId = models.AutoField(primary_key=True)
    TarefaNome = models.CharField(max_length=100)
    
class Usuarios(models.Model):
    UsuarioId = models.AutoField(primary_key=True)
    UsuarioNomme = models.CharField(max_length=100)
    Departamento = models.CharField(max_length=100)
    DataDeIngresso = models.DateField()
    ArquivoDeFoto = models.CharField(max_length=100)
    