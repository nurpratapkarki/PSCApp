from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from src.models.user import UserProfile


class UserProfileTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com"
        )
        self.profile = UserProfile.objects.create(
            google_auth_user=self.user, email="test@example.com", full_name="Test User"
        )
        self.client = APIClient()
        self.url = reverse("user-profile")

    def test_get_profile_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "test@example.com")
        self.assertEqual(response.data["full_name"], "Test User")

    def test_update_profile(self):
        self.client.force_authenticate(user=self.user)
        data = {"full_name": "Updated Name", "preferred_language": "NP"}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.profile.refresh_from_db()
        self.assertEqual(self.user.profile.full_name, "Updated Name")
        self.assertEqual(self.user.profile.preferred_language, "NP")

    def test_update_read_only_fields(self):
        self.client.force_authenticate(user=self.user)
        # Attempt to update experience_points (read-only)
        data = {"experience_points": 9999}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.profile.refresh_from_db()
        self.assertNotEqual(self.user.profile.experience_points, 9999)
