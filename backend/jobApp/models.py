from django.db import models

# Create your models here.

class JobApp(models.Model):
    company = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=100, null=False)
    url = models.TextField()
    date_applied = models.DateField()
    status = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return self.company