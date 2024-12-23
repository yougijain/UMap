"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

#testing
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),       # Route to the homepage view
    path('login/', views.login, name='login'),          # Route to the login view
    path('map/', views.map, name='map'),          # Route to the login view
    
    path('logged-in/', views.homepagelogo, name='homepagelogo'),
    path('events/', views.events, name='events'),
    path('registration/', views.registration, name='registration'),
    
    path('api/users/', include('users.urls')),       # Include URLs from users app
]