"""generated with djinit"""

from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
)

from src.admin.custom_admin import CustomAdmin
from src.api.auth.views import DevLoginView, GoogleLogin

urlpatterns = [
    path("api/auth/dev-login/", DevLoginView.as_view(), name="dev_login"),
    path("api/auth/user/", include("src.api.user.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/google/", GoogleLogin.as_view(), name="google_login"),
    path("api/", include("src.api.urls")),
    # Dashboard for moderation
    path("dashboard/", include("src.api.dashboard.urls", namespace="dashboard")),
    # JWT tokens
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
urlpatterns += [
    path("", CustomAdmin.urls),
]

# Don't show schema in production
if settings.DEBUG:
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    ]
