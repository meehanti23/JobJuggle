from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import JobAppSerializer
from .models import JobApp
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
from .forms import JobAppsForm

class JobAppView(viewsets.ModelViewSet):
    serializer_class = JobAppSerializer
    queryset = JobApp.objects.all()

class JobDeleteView(DeleteView):
    model = JobApp
    success_url = '/jobList'
    template_name = './home/job_delete.html'

class JobUpdateView(UpdateView):
    model = JobApp
    form_class = JobAppsForm
    success_url = '/jobList'
    template_name = './home/job_form.html'

class JobCreateView(CreateView):
    model = JobApp
    form_class = JobAppsForm
    success_url = '/jobList'
    template_name = './home/job_form.html'

class JobListView(ListView):
    model = JobApp
    context_object_name = "jobApps"
    template_name = './home/jobList.html'

class JobDetailView(DetailView):
    model = JobApp
    context_object_name = "job"
    template_name = './home/jobDetails.html'