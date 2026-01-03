from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class PlatformStatsApiTests(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_stats(self):
        url = reverse("platform-stats-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should contain default 0s or actual stats
        self.assertIn("total_users_active", response.data)
