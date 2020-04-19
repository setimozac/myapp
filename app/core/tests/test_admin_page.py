from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminPageTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_superuser(
            email='testadmin@test.com',
            password='testingpass123'
        )
        self.client.force_login(self.user)

    def test_admin_changelist_page(self):

        url = reverse("admin:core_myuser_changelist")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.email)

    def test_admin_change_page(self):

        url = reverse("admin:core_myuser_change", args=(self.user.pk, ))

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'testadmin@test.com')

    def test_admin_add_page(self):
        url = reverse("admin:core_myuser_add")

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
