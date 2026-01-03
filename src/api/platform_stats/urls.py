from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.platform_stats.views import PlatformStatsViewSet

router = DefaultRouter()
router.register(r"platform-stats", PlatformStatsViewSet, basename="platform-stats")

urlpatterns = [
    path("", include(router.urls)),
]
