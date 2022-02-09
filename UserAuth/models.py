from django.db import models

# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=False)
    last_name = models.CharField(max_length=250, null=True, blank=False)