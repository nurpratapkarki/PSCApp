from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.mocktest.views import MockTestViewSet

router = DefaultRouter()
router.register(r"mock-tests", MockTestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
