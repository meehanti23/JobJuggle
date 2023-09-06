from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import JobAppSerializer
from .models import JobApp
from django.http import Http404
from django.views.generic import ListView, DetailView

# Create your views here.

class JobAppView(viewsets.ModelViewSet):
    serializer_class = JobAppSerializer
    queryset = JobApp.objects.all()

class JobListView(ListView):
    model = JobApp
    context_object_name = "jobApps"
    template_name = './home/jobList.html'

class JobDetailView(DetailView):
    model = JobApp
    context_object_name = "job"
    template_name = './home/jobDetails.html'