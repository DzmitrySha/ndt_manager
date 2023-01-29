# from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from equiptypes.models import EquipType
from ndt_manager.mixins import AppLoginRequiredMixin


class EquipTypesList(ListView):
    model = EquipType
    template_name = "equiptypes/equiptypes.html"
    context_object_name = "equiptypes"
    extra_context = {'title': _('Equipment types'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateEquipType(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = EquipType
    fields = ['name']
    template_name = "equiptypes/form.html"
    success_message = _('Equipment type successfully created')
    success_url = reverse_lazy('equiptypes')
    extra_context = {'title': _('Create equipment type'),
                     'btn_name': _('Create')
                     }


class UpdateEquipType(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = EquipType
    fields = ['name']
    template_name = "equiptypes/form.html"
    success_message = _('Equipment type successfully updated')
    success_url = reverse_lazy('equiptypes')
    extra_context = {'title': _('Update equipment type'),
                     'btn_name': _('Update'),
                     }


class DeleteEquipType(SuccessMessageMixin, AppLoginRequiredMixin, DeleteView):
    model = EquipType
    template_name = "equiptypes/delete.html"
    context_object_name = "equiptype"
    success_message = _('Equipment type successfully deleted')
    success_url = reverse_lazy('equiptypes')
    extra_context = {'title': _('Delete equipment type'),
                     'btn_name': _('Yes, delete'),
                     }
