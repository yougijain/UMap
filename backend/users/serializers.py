# users/serializers.py

from rest_framework import serializers
from .models import Event, UserPreference, EventCheckIn, EventFeedback

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'

class EventCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCheckIn
        fields = '__all__'

class EventFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFeedback
        fields = '__all__'
