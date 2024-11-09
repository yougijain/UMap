# users/models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[
        ('academic', 'Academic'), 
        ('cultural', 'Cultural'),
        ('sports', 'Sports'), 
        ('social', 'Social')
    ])
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_categories = models.JSONField()

    def __str__(self):
        return f"{self.user.username}'s Preferences"

class EventCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} checked in at {self.event.title}"

class EventFeedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='event_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s feedback on {self.event.title}"
