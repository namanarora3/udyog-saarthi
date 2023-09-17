from django.shortcuts import render

from core.models import Course

from django.contrib.auth import get_user_model

from .serializers import ModelSerializer

from rest_framework import mixins, permissions, viewsets


class PublicCourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
  serializer_class = ModelSerializer
  queryset = Course.objects.all()

  def get_queryset(self):
      return self.queryset.filter(issue = self.request.user.issue)



# Create your views here.

