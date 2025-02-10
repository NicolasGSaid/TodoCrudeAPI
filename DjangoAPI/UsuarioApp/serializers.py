
#Importa o modulo serializers do rest_framework, esse mmodulo fornece classes e ferramentas para criar serializadores

from rest_framework import serializers

#Importa os modelos Tarefas e Usuarios do arquivo models.py

from UsuarioApp.models import Tarefas

#Serializer para o modelo de tarefas

class TarefaSerializer(serializers.ModelSerializer): #Define a classe TarefaSerializer, que herda de serializers.ModelSerializer
    class Meta:
        model = Tarefas # informa que esse serializer é baseado no model tarefas
        fields = '__all__' # informa que todos os campos do modelo devem ser serializados
        