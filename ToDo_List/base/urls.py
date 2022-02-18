from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('task_list', TaskList.as_view(), name='tasks'),
    path('task_detail/<int:pk>/', TaskDetail.as_view(), name='task_detail')
]
