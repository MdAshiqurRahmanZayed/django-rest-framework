from django.urls import path 
from .views import *
urlpatterns = [
    path('',HomeListAPIView.as_view(),name='HomeListAPIView'),
    path('search/',Search.as_view(),name='Search'),
    path('<str:slug>/',HomeRetrieveAPIView.as_view(),name='HomeDetailSerializer'),
    path('images/<int:pk>/',ImageApiView.as_view(),name='ImageApiView'),
]
