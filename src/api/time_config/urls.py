from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.time_config.views import TimeConfigurationViewSet

router = DefaultRouter()
router.register(r"time-configs", TimeConfigurationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
