"""Dashboard URL configuration."""

from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    # Main dashboard
    path("", views.dashboard_index, name="index"),
    # Contributions
    path("contributions/", views.contributions_list, name="contributions"),
    path(
        "contribution/<int:pk>/",
        views.contribution_detail,
        name="contribution_detail",
    ),
    path(
        "contribution/<int:pk>/approve/",
        views.approve_contribution,
        name="approve_contribution",
    ),
    path(
        "contribution/reject/",
        views.reject_contribution,
        name="reject_contribution",
    ),
    path(
        "contribution/<int:pk>/make-public/",
        views.make_public,
        name="make_public",
    ),
    path(
        "contribution/<int:pk>/feature/",
        views.feature_contribution,
        name="feature_contribution",
    ),
    # Questions
    path("questions/", views.questions_list, name="questions"),
    path("question/<int:pk>/", views.question_detail, name="question_detail"),
    path(
        "question/<int:pk>/publish/",
        views.publish_question,
        name="publish_question",
    ),
    path(
        "question/<int:pk>/verify/",
        views.verify_question,
        name="verify_question",
    ),
    path(
        "question/<int:pk>/check-duplicate/",
        views.check_duplicate,
        name="check_duplicate",
    ),
    # Reports
    path("reports/", views.reports_list, name="reports"),
    path(
        "report/<int:pk>/resolve/",
        views.resolve_report,
        name="resolve_report",
    ),
]
