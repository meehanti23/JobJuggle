from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JobAppSerializer
from .models import JobApp

# Create your views here.

class JobAppView(viewsets.ModelViewSet):
    serializer_class = JobAppSerializer
    queryset = JobApp.objects.all()