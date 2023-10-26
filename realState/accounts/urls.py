from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/',register_view,name='register'),
    # path('register/',RegisterView.as_view(),name='register'),
    path("token/", MyTokenObtainPairView.as_view(),name='MyTokenObtainPairView'),
    path("loginWithEmail/", loginWithEmail,name='loginWithEmail'),
    path("token/refresh/", TokenRefreshView.as_view(),name='TokenRefreshView'),
    path('api-token-auth/', obtain_auth_token),
    path('login/', LoginForm),
    
]
