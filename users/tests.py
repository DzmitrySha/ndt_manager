import os
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from ndt_manager.settings import FIXTURE_DIRS
from users.forms import UserCreationFormCustom
from django.utils.translation import gettext_lazy as _


class SetupTestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.create_url = reverse_lazy('create')
        self.update_pk1_url = reverse_lazy('update', kwargs={"pk": 1})
        self.delete_pk1_url = reverse_lazy("delete", kwargs={"pk": 1})
        self.delete_pk3_url = reverse_lazy("delete", kwargs={"pk": 3})
        self.login_url = reverse_lazy('login')
        self.users_url = reverse_lazy('users')
        self.users = get_user_model().objects.all()
        self.user1 = get_user_model().objects.get(pk=1)
        self.user3 = get_user_model().objects.get(pk=3)
        with open(os.path.join(FIXTURE_DIRS[0], "one_user.json")) as file:
            self.test_user = json.load(file)


class TestCreateUser(SetupTestUser):

    def test_open_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(path=self.create_url, data=self.test_user)
        self.assertRedirects(response, self.login_url, 302)
        self.user4 = get_user_model().objects.get(pk=4)
        self.assertEqual(first=self.user4.username,
                         second=self.test_user.get('username'))
        self.assertEqual(first=self.user4.first_name,
                         second=self.test_user.get('first_name'))
        self.assertEqual(first=self.user4.last_name,
                         second=self.test_user.get('last_name'))


class TestUserCreationForm(SetupTestUser):

    def test_user_create_form_with_data(self):
        user_form = UserCreationFormCustom(data=self.test_user)
        self.assertTrue(user_form.is_valid())
        self.assertEqual(len(user_form.errors), 0)

    def test_user_creation_form_with_no_data(self):
        user_form = UserCreationFormCustom(data={})
        self.assertFalse(user_form.is_valid())
        self.assertEqual(len(user_form.errors), 5)

    def test_user_creation_form_with_username_exists_error(self):
        self.test_user['username'] = self.user1.username
        user_form = UserCreationFormCustom(data=self.test_user)
        response = self.client.post(path=self.create_url, data=self.test_user)
        self.assertContains(response,
                            _('A user with that username already exists.'),
                            status_code=200)
        self.assertFalse(user_form.is_valid())
        self.assertEqual(len(user_form.errors), 1)


class TestUpdateUser(SetupTestUser):

    def test_open_update_page(self):
        # with no login
        response = self.client.get(self.update_pk1_url)
        self.assertRedirects(response, self.login_url, 302, 200)
        # with login
        self.client.force_login(self.user1)
        response = self.client.get(self.update_pk1_url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        self.client.force_login(self.user1)
        self.assertNotEqual(self.user1.username,
        self.test_user.get("username"))
        response = self.client.post(self.update_pk1_url, data=self.test_user)
        self.assertEqual(response.status_code, 302)
        self.user1 = get_user_model().objects.get(pk=1)
        self.assertEqual(self.user1.username, self.test_user.get("username"))

    def test_update_other_user(self):
        self.client.force_login(self.user3)
        response = self.client.post(self.update_pk1_url, data=self.test_user)
        self.assertRedirects(response, self.users_url, 302, 200)


# class TestDeleteUser(SetupTestUser):
#     fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']
#
#     def test_open_delete_page(self):
#         # with no login
#         response = self.client.get(self.delete_pk1_url)
#         self.assertRedirects(response, self.login_url, 302)
#         # with login (self delete user)
#         self.client.force_login(self.user1)
#         response = self.client.get(self.delete_pk1_url)
#         self.assertEqual(response.status_code, 200)
#         # with login (delete other user)
#         self.client.force_login(self.user3)
#         response = self.client.get(self.delete_pk1_url)
#         self.assertEqual(response.status_code, 302)
#
#     def test_delete_user(self):
#         self.client.force_login(self.user3)
#         response = self.client.delete(self.delete_pk3_url)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(self.users.count(), 2)
#         with self.assertRaises(get_user_model().DoesNotExist):
#             get_user_model().objects.get(pk=3)
#
#     def test_delete_other_user(self):
#         self.client.force_login(self.user3)
#         response = self.client.post(self.delete_pk1_url)
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(self.users.count(), 3)
