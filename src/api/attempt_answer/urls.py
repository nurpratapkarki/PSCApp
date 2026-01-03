from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.attempt_answer.views import UserAnswerViewSet, UserAttemptViewSet

router = DefaultRouter()
router.register(r"attempts", UserAttemptViewSet, basename="attempt")
router.register(r"answers", UserAnswerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
