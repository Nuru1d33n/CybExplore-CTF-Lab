# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('task/<int:pk>/', views.task_detail, name='task_detail'),
#     path('task/<int:pk>/submit/', views.submit_task, name='submit_task'),
#     path('leaderboard/', views.leaderboard, name='leaderboard'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabCategoryViewSet, LabTaskViewSet, ProgressViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'labcategories', LabCategoryViewSet)
router.register(r'labtasks', LabTaskViewSet)
router.register(r'progress', ProgressViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
