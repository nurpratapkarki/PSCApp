from django.urls import include, path

urlpatterns = [
    path("auth/", include("src.api.user.urls")),
    path("", include("src.api.branch.urls")),
    path("", include("src.api.question_answer.urls")),
    path("", include("src.api.mocktest.urls")),
    path("", include("src.api.attempt_answer.urls")),
    path("", include("src.api.user_stats.urls")),
    path("", include("src.api.notification.urls")),
    path("", include("src.api.platform_stats.urls")),
    path("analytics/", include("src.api.analytics.urls")),
    path("config/", include("src.api.app_settings.urls")),
    path("config/", include("src.api.time_config.urls")),
]
