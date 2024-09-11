from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/submit/', views.submit_task, name='submit_task'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
