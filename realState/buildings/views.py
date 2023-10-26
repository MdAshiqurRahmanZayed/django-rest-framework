from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions,status
from rest_framework.views import APIView
from rest_framework.generics import *
from buildings.models import *
from buildings.serializers import *
from rest_framework.response import Response
from django.db.models import query,Q


class HomeListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,) 
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = HomeSerializer
    lookup_field = 'slug'



class HomeRetrieveAPIView(RetrieveAPIView):
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = HomeDetailSerializer
    lookup_field = 'slug'
    
class ImageApiView(APIView):
     def get(self,request,pk,format=None):
          home = Home.objects.get(pk=pk)
          images = home.images.all()
          serializer = ImageFilesSerializer(images,many = True)
          return Response(serializer.data,status=status.HTTP_200_OK) 




class Search(APIView):
     permission_classes = (permissions.IsAuthenticated,)
     def post(self,request,format=None):
        data=self.request.data
        queryset=Home.objects.filter(is_published=True)
        try:
            str=data['str']
            q= (Q(description__icontains=str)) | (Q(title__icontains=str))
            queryset=queryset.filter(q)
        except:
            pass
        try:
            price_from=data['price_from']
            queryset=queryset.filter(price__gte=price_from)
        except:
            pass
        try:
            price_to=data['price_to']
            queryset=queryset.filter(price__lte=price_to)
        except:
            pass
        try:
            city=data['city']
            queryset=queryset.filter(cit__icontains=city)
        except:
            pass
        serializer=HomeSerializer(queryset,many=True)
        return Response(serializer.data)