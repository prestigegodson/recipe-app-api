from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_and_password(self):
        """Test if the create user  method of user model works"""

        email = 'prestigegodson@gmail.com'
        password = 'otuonye'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_email_normalize(self):
        email = 'prestigegodson@GMAIL.COM'
        password = 'otuonye'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_super_user(self):
        """Test if super user is created"""
        user = get_user_model().objects.create_superuser(email='admin@1234', password='adminpassword')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
