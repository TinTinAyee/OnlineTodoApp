from django.contrib import admin
from django.urls import path

from .import views 

urlpatterns = [

    path('home/',views.todo_list),
    path('list/',views.add_todo_item,name='add_todo_item'),
    path('delete/<int:todo_id>',views.delete_todo_item, name='delete_todo_item')
    
]