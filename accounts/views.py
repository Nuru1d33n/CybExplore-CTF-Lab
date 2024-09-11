# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required

# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form': form})


# from django.contrib.auth import logout



# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})


from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email.html'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('password_reset_complete')

    def post(self, request, *args, **kwargs):
        # Customize the response or behavior if needed
        return super().post(request, *args, **kwargs)
