from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.list_url = reverse('v1:course-list')
        self.user = User.objects.create_user(username='test', password='test')

    def test_authentication_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authentication_user_invalid(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authentication_user_invalid_password(self):
        user = authenticate(username='test', password='test_2')
        self.assertFalse(user)

    def test_authentication_user_valid(self):
        user = authenticate(username='test', password='test')
        self.assertTrue(user)
