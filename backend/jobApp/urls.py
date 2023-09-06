from django.urls import path
from . import views

urlpatterns = [
    path('jobList', views.JobListView.as_view()),
    path('jobList/<int:pk>', views.JobDetailView.as_view()),
]