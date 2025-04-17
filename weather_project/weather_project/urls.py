"""
URL configuration for weather_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('weather_data.urls')),  # This includes your weather app at root
# ]

from django.contrib import admin
from django.urls import path, include
from weather_data.views import weather_table_view  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather_data.urls')),  # API routes under /api/
    path('', weather_table_view, name='weather-home'),  # Root URL goes directly to your view
]
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('weather_data.urls')),  # Changed from 'api/' to root
# ]