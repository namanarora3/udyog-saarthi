from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()

urlpatterns = [
  path('create/', views.CreateUserView.as_view(), name='create'),
  path('authenticate/', views.CreateTokenView.as_view(), name='authenticate'),
]