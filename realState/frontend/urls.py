from django.urls import path,include
from .views import *


urlpatterns = [
    path('',contactRequest,name='contactRequest'),
    path('login/', login, name='login'),
]
