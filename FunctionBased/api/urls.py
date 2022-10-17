from django.urls import path
from .views import apiOverview,ToDoList,ToDoDetail,ToDoCreate,ToDoUpdate,ToDoDelete

urlpatterns = [
     path('',apiOverview,name="api-overview"),
     path('todo-list/', ToDoList, name="todo-list"),
     path('todo-create/', ToDoCreate, name="todo-create"),
     path('todo-detail/<int:pk>',  ToDoDetail, name="todo-detail"),
     path('todo-update/<int:pk>',  ToDoUpdate, name="todo-update"),
     path('todo-delete/<int:pk>',  ToDoDelete, name="todo-delete"),
     
]