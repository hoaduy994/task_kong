from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogList.as_view(), name='blog-list'),
    path('create/', BlogCreate.as_view(), name='blog-create'),
    path('<int:pk>/update/', BlogUpdate.as_view(), name='blog-update'),
    path('<int:pk>/delete/', BlogDelete.as_view(), name='blog-delete'),
]