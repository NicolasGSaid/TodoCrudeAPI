from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UsuarioApp.models import Tarefas, Usuarios
from UsuarioApp.serializers import TarefaSerializer, UsuarioSerializer

from django.core.files.storage import default_storage



# Create your views here.

@csrf_exempt
def tarefaApi(request,id=0):
    if request.method=='GET':
        tarefas = Tarefas.objects.all()
        tarefas_serializer = TarefaSerializer(tarefas, many=True)
        return JsonResponse(tarefas_serializer.data, safe=False)
    
    elif request.method=="POST":
        tarefa_data = JSONParser().parse(request)
        tarefa_serializer = TarefaSerializer(data=tarefa_data)
        if tarefa_serializer.is_valid():
            tarefa_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        
    elif request.method=="PUT":
        tarefa_data = JSONParser().parse(request)
        tarefa = Tarefas.objects.get(TarefaId=tarefa_data['TarefaId'])
        tarefa_serializer = TarefaSerializer(tarefa, data=tarefa_data)
        if tarefa_serializer.is_valid():
            tarefa_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)
    
    elif request.method=="DELETE":
        tarefa = Tarefas.objects.get(TarefaId=id)
        tarefa.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    
@csrf_exempt
def usuarioApi(request, id=0):
    if request.method == 'GET':
        usuarios = Usuarios.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(usuarios_serializer.data, safe=False)

    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Adicionado com sucesso", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    
    elif request.method == 'PUT':
        usuario_data = JSONParser().parse(request)
        usuario = Usuarios.objects.get(UsuarioId=usuario_data['UsuarioId'])
        usuario_serializer = UsuarioSerializer(usuario, data=usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar", safe=False)

    elif request.method == 'DELETE':
        usuario = Usuarios.objects.get(UsuarioId=id)
        usuario.delete()
        return JsonResponse("Deletado com sucesso", safe=False)
    
@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False) 
