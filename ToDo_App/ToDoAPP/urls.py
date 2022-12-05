
from django.urls import path

from ToDoAPP import views


app_name = 'ToDoAPP'
urlpatterns = [
    path('', views.task, name='task'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('classhome/', views.TaskListView.as_view(), name='classhome'),
    path('classdetailview/<int:pk>/', views.TaskDetailView.as_view(), name='classdetailview'),
    path('updateview/<int:pk>/', views.TaskUpdateView.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.TaskDeleteView.as_view(), name='deleteview')

]

