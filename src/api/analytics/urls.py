from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.analytics.views import ContributionViewSet, DailyActivityViewSet

router = DefaultRouter()
router.register(r"contributions", ContributionViewSet)
router.register(r"daily-activity", DailyActivityViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
