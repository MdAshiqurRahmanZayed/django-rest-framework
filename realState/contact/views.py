from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.response import Response 
from rest_framework.views import APIView 
from rest_framework import permissions
from .serializers import *

class ContactAPIView(APIView):
     permission_classes = (permissions.IsAuthenticated,)
     def get(self,request,format=None):
          queryset = Contact.objects.all()
          serializers = ContactSerializer(queryset,many=True)
          return Response(serializers.data)
     def post(self,request,format=None):
          serializers = ContactSerializer(data=request.data)
          if serializers.is_valid():
               serializers.save()
               return Response(serializers.data,status=status.HTTP_201_CREATED)
          return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


