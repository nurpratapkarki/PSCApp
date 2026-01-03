from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.app_settings.views import AppSettingsViewSet

router = DefaultRouter()
router.register(r"settings", AppSettingsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
