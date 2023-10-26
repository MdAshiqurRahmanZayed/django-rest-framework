from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView  
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
import requests,json

@api_view(['POST'])
def register_view(request):
     if request.method == 'POST':
          serializers = RegisterSerializer(data = request.data)
          data = {}
          
          if serializers.is_valid(raise_exception=True):
               user = serializers.save()
               data['response'] = "Successfully done"
               data['username'] = f'{user}'
               data['email'] = serializers.data['email']
          else:
               data = serializers.errors
          return Response(data) 
     
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
               
          
          

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
     # def validate(self,attrs):
    def validate(self, attrs):
        email = attrs.get('email') 
        password = attrs.get('password')
     #    self.user
        print(email,password)
        print(attrs)
        username_field = get_user_model().USERNAME_FIELD
        print(username_field)  
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['type'] = 'Bearer'
        data['lifetime'] = str(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].days) + ' days'
        
        # Include additional user data here
        data['user_id'] = self.user.id
        data['user_email'] = self.user.email
        data['user_username'] = self.user.username
        
        return data 
        
 

class MyTokenObtainPairView(TokenObtainPairView):
     serializer_class = MyTokenObtainPairSerializer 
     

# log in with email
@api_view(['POST'])
def loginWithEmail(request):
     if request.method == 'POST':
          # print(request.data)
          try:
               email = request.data.get('email')
               password = request.data.get('password')
               username = email.split('@')[0]+'_'+email.split('@')[1].split('.')[0]
               url = 'http://127.0.0.1:8000/api/accounts/token/'
               data = {
                    "username" : username,
                    "password" : password
               }
               api  = requests.post(url=url,data=data)
               try:
                    resp = json.loads(api.text)
                    return Response(resp) 
               except:
                    return Response({"erros":"bad request"})
          except:
                    return Response({"erros":"bad request"})
     return Response({"test":"hello"})

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')