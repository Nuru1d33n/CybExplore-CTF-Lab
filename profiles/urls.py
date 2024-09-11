from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.view_profile, name='view_profile'),
    path('notifications/', views.notifications, name='notifications'),
]
