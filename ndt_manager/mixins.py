from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class AppLoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        messages.error(
            self.request,
            _('You are not logged in. Please log in.')
        )
        return redirect(self.login_url)
