from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('task-list', TaskList.as_view(), name='task-list'),
    path('task-detail/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-create/', TaskCreate.as_view(), name='task-create')
]
