# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Correctly importing views from the current directory

# Create a router to register viewsets
router = DefaultRouter()
router.register(r'events', views.EventViewSet, basename='event')
router.register(r'preferences', views.UserPreferenceViewSet, basename='preference')
router.register(r'feedback', views.EventFeedbackViewSet, basename='feedback')

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all viewsets registered with the router
    path('check-in/<int:event_id>/', views.CheckInView.as_view(), name='check-in'),  # Custom check-in endpoint
    path('events/<int:event_id>/feedback/', views.EventFeedbackViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-feedback'),
]
