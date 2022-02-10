from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True, blank=False)

    class Meta:
        db_table = 'UserProfile'

    def __str__(self) -> str:
        return self.user.username
