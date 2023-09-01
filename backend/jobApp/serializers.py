from rest_framework import serializers
from .models import JobApp

class JobAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApp
        fields = ('id', 'company', 'position', 'url', 'date_applied', 'status', 'notes')