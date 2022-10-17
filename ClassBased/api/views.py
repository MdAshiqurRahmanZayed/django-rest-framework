# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ToDo.models import ToDo
from .serializers import  TodoSerializer
from rest_framework import viewsets



@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/todo/',
		'Create':'/todo/create/',
		'Detail-View':'/todo/<str:pk>/',
		'Update':'/todo/<str:pk>/',
		'Delete':'/todo/<str:pk>/',
		}

	return Response(api_urls)



class ToDoView(viewsets.ModelViewSet):
     serializer_class = TodoSerializer
     queryset = ToDo.objects.all()     
     
