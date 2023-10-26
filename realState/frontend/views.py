from django.shortcuts import render,redirect
from .forms import ContactForm,UserLoginForm
import requests,json
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib import auth

@login_required(login_url = 'login')
def contactRequest(request):
     
     if request.method == 'POST':
          token = request.POST.get('token')
          # print(token)
          form = ContactForm(request.POST)
          user = {
               "username":request.user
          } 
          data = form.data
          url  = 'http://127.0.0.1:8000/api/contact/'
          api  = requests.post(url=url,data=data,headers={'Authorization':f'Token {token}'})
          try:
               resp = json.loads(api.text)
          except:
               resp = None
          # print(resp)
          return redirect('contactRequest')
     form = ContactForm()
     context = {
          'form':form,
     }
     return render(request,'contact.html',context)


def login(request):
     print(request.method)
     if request.method == 'POST':
          email = request.POST.get('email')
          password = request.POST.get('password')
          try:
               user = auth.authenticate(email = email,password=password)
          except:
               return redirect('login')
          try:
               user = auth.authenticate(username = email,password=password)
          except:
               return redirect('login')
          if user is not None:
               auth.login(request,user)
               return redirect('contactRequest')
          
          
          else:
               return redirect('login')
     context={
          'form':UserLoginForm
     }
     return render(request,'login.html',context)
     