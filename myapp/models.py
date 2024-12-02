from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.CharField(max_length=255)  # e.g., subjects like Math, Physics
    availability = models.TextField()  # e.g., preferred times/days for study groups

    def __str__(self):
        return self.user.username

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    date = models.DateTimeField(null=True, blank=True)  # Allow null and blank values
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
