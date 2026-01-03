from django.urls import path

from src.api.user.views import GoogleLoginView, LogoutView, UserProfileDetailView

urlpatterns = [
    path("auth/user/", UserProfileDetailView.as_view(), name="user-profile"),
    path("auth/google/", GoogleLoginView.as_view(), name="google-login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
]
