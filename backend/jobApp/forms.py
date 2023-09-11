from django import forms
from .models import JobApp

class JobAppsForm(forms.ModelForm): 
    class Meta:
        model = JobApp
        fields = ('company', 'position', 'url', 'date_applied', 'status', 'notes')
        labels = {
            'date_applied': 'Date Applied:',
            }