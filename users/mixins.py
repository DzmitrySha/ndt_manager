from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserPermissionsMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You don\'t have the rights to change another user.'))
            return redirect('users')
        else:
            messages.error(
                self.request,
                _('You are not logged in. Please log in.')
            )
            return redirect(self.login_url)
