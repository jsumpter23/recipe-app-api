from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):

        # instantiate django test client which acts as a dummy browser
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="email@email.com",
            password = "password"
        )
        

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="email2@email.com",
            password="password2",
            name="test user"
        )

    def test_users_listed(self):
        """test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # checks that http response was 200 and response includes content
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """testing if create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)