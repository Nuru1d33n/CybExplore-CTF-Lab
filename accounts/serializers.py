from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginSerializer(LoginSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
