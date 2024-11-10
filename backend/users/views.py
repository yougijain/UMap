from django.shortcuts import render

# Create your views here.

# users/views.py

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Event, UserPreference, EventCheckIn, EventFeedback
from .serializers import EventSerializer, UserPreferenceSerializer, EventCheckInSerializer, EventFeedbackSerializer
from django.http import HttpResponse
from django.shortcuts import render


# OUR PAGES:

def homepage(request):
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')






# ------------- testing and misc -----------------

def home_view(request):
    return HttpResponse("<h1>Welcome to UMap: Your Ultimate Campus Event Navigator</h1><p>Use /api/users/ to access the available endpoints.</p>")

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UserPreferenceViewSet(viewsets.ModelViewSet):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CheckInView(APIView):
    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        EventCheckIn.objects.create(user=request.user, event=event)
        return Response({"message": "Check-in successful"}, status=status.HTTP_201_CREATED)

class EventFeedbackViewSet(viewsets.ModelViewSet):
    queryset = EventFeedback.objects.all()
    serializer_class = EventFeedbackSerializer

    def get_queryset(self):
        return self.queryset.filter(event_id=self.kwargs['event_id'])
