from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from rest_framework.generics import *
from .models import Agent
from .serializers import *


class AgentListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None 
    

class AgentRetrieveAPIView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class TopSellerAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Agent.objects.filter(top_seller = True)
    serializer_class = AgentSerializer
    pagination_class = None 
    


