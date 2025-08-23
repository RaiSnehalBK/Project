from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    experience = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20, blank=True)
    pager = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username
