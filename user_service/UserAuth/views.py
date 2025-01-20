from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Blog
from django.contrib.auth.models import User
from .serializers import BlogSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserRegiste(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class Login(TokenObtainPairView):
    permission_classes = []
    
class RefreshTokenView(TokenRefreshView):
    permission_classes = []