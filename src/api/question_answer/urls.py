from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.question_answer.views import QuestionReportViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r"questions", QuestionViewSet)
router.register(r"reports", QuestionReportViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
