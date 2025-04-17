from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WeatherRecordViewSet

router = DefaultRouter()
router.register(r'weather', WeatherRecordViewSet)

urlpatterns = router.urls

# from django.urls import path
# from .views import weather_table_view

# urlpatterns = [
#     path('', weather_table_view, name='weather-home'),  # This will handle the root URL
# ]


# from django.urls import include, path
# from .views import weather_table_view, WeatherRecordViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'weather', WeatherRecordViewSet)

# urlpatterns = [
#     path('weather-table/', weather_table_view, name='weather-table'),
#     path('api/', include(router.urls)),  # This will include all API routes
# ]