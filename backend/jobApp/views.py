from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import JobAppSerializer
from .models import JobApp

# Create your views here.

class JobAppView(viewsets.ModelViewSet):
    serializer_class = JobAppSerializer
    queryset = JobApp.objects.all()

def jobList(request):
    return render(request, 'home/welcome.html', {})