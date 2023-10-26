from django.urls import path,include
from .views import *
urlpatterns = [
    path('',ContactAPIView.as_view(),name='all-contact'),
]
