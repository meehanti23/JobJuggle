from django.urls import path
from . import views

urlpatterns = [
    path('jobList', views.JobListView.as_view(), name="jobApps.list"),
    path('jobList/<int:pk>', views.JobDetailView.as_view(), name="jobApps.detail"),
    path('jobList/<int:pk>/edit', views.JobUpdateView.as_view(), name="jobApps.update"),
    path('jobList/<int:pk>/delete', views.JobDeleteView.as_view(), name="jobApps.delete"),
    path('jobList/new', views.JobCreateView.as_view(), name="job.new"),
]