from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminPageTests(TestCase):

    def setUp(self):
        self.client = Client()
        user = get_user_model().objects.create_superuser(
            email='testadmin@test.com',
            password='testingpass123'
        )
        self.client.force_login(user)

    def test_admin_changelist_page(self):

        url = reverse("admin:core_myuser_changelist")
        print(url)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
