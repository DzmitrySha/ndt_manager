from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from stations.models import Station
from ndt_manager.mixins import AppLoginRequiredMixin


class StationsList(AppLoginRequiredMixin, ListView):
    model = Station
    template_name = "stations/stations.html"
    context_object_name = "stations"
    extra_context = {'title': _('Stations'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateStation(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = Station
    fields = ['name', 'address']
    template_name = "stations/form.html"
    success_message = _('Station successfully created')
    success_url = reverse_lazy('stations')
    extra_context = {'title': _('Create station'),
                     'btn_name': _('Create')
                     }


class UpdateStation(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = Station
    fields = ['name', 'address']
    template_name = "stations/form.html"
    success_message = _('Station successfully updated')
    success_url = reverse_lazy('stations')
    extra_context = {'title': _('Update station'),
                     'btn_name': _('Update'),
                     }


class DeleteStation(SuccessMessageMixin, AppLoginRequiredMixin, DeleteView):
    model = Station
    template_name = "stations/delete.html"
    success_url = reverse_lazy('stations')
    success_message = _('Station successfully deleted')
    context_object_name = "station"
    extra_context = {'title': _('Delete station'),
                     'btn_name': _('Yes, delete'),
                     }

    def post(self, request, *args, **kwargs):
        if self.get_object().stations.count():
            messages.error(
                self.request,
                _('It`s not possible to delete the station that is being used')
            )
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
