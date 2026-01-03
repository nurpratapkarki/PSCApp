from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = (
        getattr(settings, "GOOGLE_OAUTH_CALLBACK_URL", None)
        or "http://localhost:8000/accounts/google/login/callback/"
    )
    client_class = OAuth2Client


class DevLoginView(APIView):
    """
    Development-only view to simulate Google Login without actual Google interaction.
    Accepts an email, creates/gets a user, and returns tokens.
    """

    permission_classes = (AllowAny,)
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        # We handle logic manually, so APIView is cleaner.
        if not settings.DEBUG:
            return Response({"error": "Not available in production"}, status=403)

        email = request.data.get("email")
        if not email:
            return Response({"error": "Email required"}, status=400)

        # Simulate user retrieval/creation
        from django.contrib.auth import get_user_model

        User = get_user_model()

        user, created = User.objects.get_or_create(username=email, email=email)
        if created:
            user.set_unusable_password()
            user.save()

        from dj_rest_auth.utils import jwt_encode

        access_token, refresh_token = jwt_encode(user)

        data = {
            "user": {
                "pk": user.pk,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            "access": str(access_token),
            "refresh": str(refresh_token),
        }
        return Response(data)

        data = {
            "user": {
                "pk": user.pk,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            "access": str(self.access_token),
            "refresh": str(self.refresh_token),
        }
        return Response(data)
