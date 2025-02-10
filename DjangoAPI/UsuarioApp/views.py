from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UsuarioApp.models import Tarefas
from UsuarioApp.serializers import TarefaSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def tarefaApi(request, id=0): #request representa a requisição HTTP feita pelo front, id é usado para identificar a tarefa
    
    if request.method=='GET':  #requisição de leitura      
        tarefas = Tarefas.objects.all() #obtém todas as tarefas do banco 
        tarefas_serializer = TarefaSerializer(tarefas, many=True)   # serializa as instancias para JSON    
        return JsonResponse(tarefas_serializer.data, safe=False) #retorna as tarefas serializadas em JSON
    
    elif request.method=="POST":  #requisição de criação, nesse caso tarefa       
        tarefa_data = JSONParser().parse(request) # Converte os dados json para um formato python, contendo as infos da nova tarefa 
        tarefa_serializer = TarefaSerializer(data=tarefa_data) # cria uma instancia serializer passando dos dados para validação 
        
        if tarefa_serializer.is_valid(): #verifica se os dados sao validos          
            tarefa_serializer.save() # salva no banco 
            return JsonResponse("Adicionado com sucesso", safe=False) #retorna uma mensagem de sucesso
        return JsonResponse("Falha ao adicionar", safe=False) #retorna uma mensagem de falha
        
    elif request.method=="PUT":   #requisição de atualização
        tarefa_data = JSONParser().parse(request) # Converte os dados json para um formato python, contendo as novas infos da tarefa
        tarefa = Tarefas.objects.get(TarefaId=tarefa_data['TarefaId']) # Busca a tarefa no banco de dados pelo id 
        tarefa_serializer = TarefaSerializer(tarefa, data=tarefa_data) # cria uma instancia serializer passando dos dados para validação
        
        if tarefa_serializer.is_valid(): #verifica se os dados sao validos
            tarefa_serializer.save()    # salva no banco
            return JsonResponse("Atualizado com sucesso", safe=False) #retorna uma mensagem de sucesso
        return JsonResponse("Falha ao atualizar", safe=False) #retorna uma mensagem de falha
    
    elif request.method=="DELETE": # requisição de deleção
        tarefa = Tarefas.objects.get(TarefaId=id) # Busca a tarefa no banco de dados pelo id
        tarefa.delete() # deleta a tarefa encontrada no banco 
        return JsonResponse("Deletado com sucesso", safe=False) # retorna uma mensagem de sucesso na deleção 
    
