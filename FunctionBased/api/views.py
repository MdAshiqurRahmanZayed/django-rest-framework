from urllib import response
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoSerializer

from ToDo.models import ToDo
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/todo-list/',
		'Detail View':'/todo-detail/<str:pk>/',
		'Create':'/todo-create/',
		'Update':'/todo-update/<str:pk>/',
		'Delete':'/todo-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def ToDoList(request):
	todo = ToDo.objects.all()
	serializer = ToDoSerializer(todo, many = True)
	return Response(serializer.data)
@api_view(['GET'])
def ToDoDetail(request,pk):
	todo = ToDo.objects.get(id=pk)
	serializer = ToDoSerializer(todo, many = False)
	return Response(serializer.data)

@api_view(['POST'])
def ToDoCreate(request):
     serilazer = ToDoSerializer(data = request.data)
     if serilazer.is_valid():
          serilazer.save()
     return Response(serilazer.data)

@api_view(['POST'])
def ToDoUpdate(request,pk):
     todo = ToDo.objects.get(id=pk)
     serilazer = ToDoSerializer(instance=todo, data = request.data)
     if serilazer.is_valid():
          serilazer.save()
          
     return Response(serilazer.data)

@api_view(['DELETE'])
def ToDoDelete(request,pk):
     todo = ToDo.objects.get(id = pk )
     todo.delete()
     return Response('Item succsesfully delete!')
