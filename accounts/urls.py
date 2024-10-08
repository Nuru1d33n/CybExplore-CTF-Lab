# from django.urls import path
# from accounts import views
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('login/', views.login, name='login'),
#     path('register/', views.register, name='register'),

#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]


from django.urls import path
from accounts.views import CustomPasswordResetView, CustomPasswordResetConfirmView

urlpatterns = [
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
