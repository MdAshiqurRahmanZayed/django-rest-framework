from django.urls import path,include
from .views import ToDoView,apiOverview
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', ToDoView, 'todo')

urlpatterns = [
     path('api/',apiOverview,name="api"),
     path('api/',include(router.urls),name='api-all')
]