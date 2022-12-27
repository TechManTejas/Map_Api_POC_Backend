from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from locations import views as locations_views

router = DefaultRouter()
router.register('locations', locations_views.LocationModelViewset, basename='locations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
