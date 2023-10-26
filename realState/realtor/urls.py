from django.urls import path,include
from .views import *
urlpatterns = [
    path('',AgentListAPIView.as_view(),name='agents'),
    path('<int:pk>/',AgentRetrieveAPIView.as_view(),name='AgentRetrieveAPIView'),
    path('topseller/',TopSellerAPIView.as_view(),name='TopSellerAPIView'),
]
