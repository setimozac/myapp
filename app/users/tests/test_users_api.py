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

    def test_public_authentication_endpoint(self):
        url = reverse("users:token")

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_authenticate_successfull(self):
        url = reverse("users:token")
        get_user_model().objects.create_user(**self.payload)

        res = self.client.post(url, self.payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('token', res.data)
        self.assertNotIn('password', res.data)

    def test_token_invalid_payload(self):
        url = reverse("users:token")

        res = self.client.post(url, {})

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn('token', res.data)


class PrivateUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@test.com',
            password='testingpass123',
            name='test user'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
