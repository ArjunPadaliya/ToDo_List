from django.urls import path
from .views import TaskList

urlpatterns = [
    path('task_list', TaskList.as_view(), name='tasks')
]
