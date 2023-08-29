from django.contrib import admin
from .models import JobApp

class JobAppAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'url', 'date_applied', 'status', 'notes')

# Register your models here.

admin.site.register(JobApp, JobAppAdmin)