from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.user_stats.views import (
    LeaderBoardViewSet,
    StudyCollectionViewSet,
    UserProgressViewSet,
    UserStatisticsViewSet,
)

router = DefaultRouter()
router.register(r"statistics", UserStatisticsViewSet, basename="user-statistics")
router.register(r"progress", UserProgressViewSet, basename="user-progress")
router.register(r"collections", StudyCollectionViewSet, basename="study-collection")
router.register(r"leaderboard", LeaderBoardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
