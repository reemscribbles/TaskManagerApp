from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, HabitCreate, HabitDelete, HabitUpdate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path("", TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
     path('habit-create/', HabitCreate.as_view(), name="habit-create"),
    path('habit-update/<int:pk>/', HabitUpdate.as_view(), name="habit-update"),
    path('habit-delete/<int:pk>/', HabitDelete.as_view(), name="habit-delete"),
    
]