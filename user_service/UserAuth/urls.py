from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegiste.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token-refresh'),
]
