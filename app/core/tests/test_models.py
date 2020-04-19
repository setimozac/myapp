from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserModeltests(TestCase):

    def setUp(self):
        self.data = {
            'email': 'testemail@company.com',
            'password': 'testinpass123',
        }

    def test_create_user_with_email(self):
        # test that user is created with email
        get_user_model().objects.create_user(**self.data)

        user = get_user_model().objects.get(email='testemail@company.com')

        self.assertTrue(user.check_password('testinpass123'))

    def test_normalized_email(self):
        self.data['email'] = 'testemail@COMPANY.COM'
        get_user_model().objects.create_user(**self.data)

        user = get_user_model(). \
            objects.get(email='testemail@company.com')

        self.assertFalse(user.is_superuser)
        self.assertEqual(user.email, self.data['email'].lower())

    def test_create_superuser(self):
        get_user_model().objects.create_superuser(**self.data)

        user = get_user_model(). \
            objects.get(email='testemail@company.com')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_no_email_fails(self):
        self.data['email'] = ''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(**self.data)
