# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from rest_framework.fields import ImageField
# from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer, RegisterSerializer
# from rest_framework import viewsets

# Register API
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AuthSerializer, RegisterSerializer
from .models import Registerextend
# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Registerextend.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = AuthSerializer
    queryset = User.objects.all()

