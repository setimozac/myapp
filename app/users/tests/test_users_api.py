from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


class PublicUserApiTests(TestCase):

    def setUp(self):
        self.payload = {
            'email': 'testuser@test.com',
            'password': 'testpass123!',
            'name': 'test user'
        }
        self.client = APIClient()

    def test_create_user_successful(self):
        url = reverse("users:create")
        res = self.client.post(url, self.payload)

        user_exists = get_user_model().objects.filter(
            email='testuser@test.com').exists()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user_exists)
        self.assertNotIn('password', res.data)
        self.assertEqual('testuser@test.com', res.data['email'])

    def test_create_user_already_exists(self):
        url = reverse("users:create")
        get_user_model().objects.create(**self.payload)
        res = self.client.post(url, self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_invalide_data(self):
        self.payload['email'] = ""
        url = reverse("users:create")

        res = self.client.post(url, self.payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_short_password(self):
        self.payload['password'] = 'lt8chr'
        url = reverse("users:create")
        res = self.client.post(url, self.payload)

        user_exists = get_user_model().objects.filter(
            email=self.payload['email']).exists()

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(user_exists)
