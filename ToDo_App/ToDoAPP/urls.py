
from django.urls import path

from ToDoAPP import views


app_name = 'ToDoAPP'
urlpatterns = [
    path('', views.task, name='task'),
    path('delete/<int:id>/', views.delete, name='delete')
]

