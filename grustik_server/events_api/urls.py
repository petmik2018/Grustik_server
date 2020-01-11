from django.urls import path, include

from rest_framework.routers import DefaultRouter

from events_api import views

router = DefaultRouter()
router.register('event', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls))
]

