from django.urls import path
from api import views

urlpatterns = [
    path('api/task_lists', views.TaskListt.as_view()),
    path('api/task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('api/task_lists/<int:pk>/tasks', views.Task.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    #path('register/',views.signup)
]