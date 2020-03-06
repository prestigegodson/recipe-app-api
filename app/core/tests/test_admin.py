from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):
    """Testing admin"""

    def setUp(self) -> None:
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='adminpassword123'
        )
        self.client.force_login(self.admin)
        self.user = get_user_model().objects.create_user(
            email='user@gmail.com',
            name='User',
            password='userpassword123'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)
