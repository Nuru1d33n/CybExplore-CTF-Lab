# from django.urls import path
# from profiles import views

# urlpatterns = [
#     path('', views.profile, name='profile'),
#     path('edit/', views.edit_profile, name='edit_profile'),
#     path('<str:username>/', views.view_profile, name='view_profile'),
#     path('notifications/', views.notifications, name='notifications'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
