from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
