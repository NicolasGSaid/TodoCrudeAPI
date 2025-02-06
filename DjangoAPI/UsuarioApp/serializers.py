from rest_framework import serializers
from UsuarioApp.models import Tarefas, Usuarios

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefas
        fields = ('TarefaId',
                  'TarefaNome')
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('UsuarioId',
                  'UsuarioNome',
                  'Departamento',
                  'DataDeIngresso',
                  'ArquivoDeFoto')
        