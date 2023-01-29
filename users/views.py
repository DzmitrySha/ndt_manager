from django.contrib import messages
from django.contrib.auth import get_user_model

from users.mixins import UserPermissionsMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)

from users.forms import UserCreationFormCustom
from ndt_manager.mixins import AppLoginRequiredMixin


class UsersList(ListView):
    model = get_user_model()
    template_name = "users/users.html"
    context_object_name = "users"
    extra_context = {'title': _('Users'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "users/user.html"
    context_object_name = "user"
    extra_context = {'title': _('User card'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationFormCustom
    template_name = "users/form.html"
    success_url = reverse_lazy('login')
    success_message = _('User successfully registered')
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }


class UpdateUser(SuccessMessageMixin, UserPermissionsMixin,
                 AppLoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserCreationFormCustom
    success_url = reverse_lazy('users')
    success_message = _('User successfully updated')
    template_name = "users/form.html"
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }


class DeleteUser(SuccessMessageMixin, UserPermissionsMixin,
                 AppLoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = "users/delete.html"
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    context_object_name = "user"
    extra_context = {'title': _('Delete user'),
                     'btn_name': _('Yes, delete'),
                     }

    def post(self, request, *args, **kwargs):

        if self.get_object().authors.count() \
                or self.get_object().executors.count():
            messages.error(
                self.request,
                _('It`s not possible to delete a User that is being used')
            )
            return redirect(self.success_url)

        return super().post(request, *args, **kwargs)
