# users/admin.py

from django.contrib import admin
from .models import Event, UserPreference, EventCheckIn, EventFeedback

admin.site.register(Event)
admin.site.register(UserPreference)
admin.site.register(EventCheckIn)
admin.site.register(EventFeedback)
