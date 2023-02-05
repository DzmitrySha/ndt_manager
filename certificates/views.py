from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from certificates.models import Certificate
from ndt_manager.mixins import AppLoginRequiredMixin


class CertificatesList(ListView):
    model = Certificate
    template_name = "certificates/certificates.html"
    context_object_name = "certificates"
    extra_context = {'title': _('Certificates'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateCertificate(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = Certificate
    fields = ['number', 'method', 'level', 'start_date', 'finish_date', 'owner', ]
    template_name = "certificates/form.html"
    success_message = _('Certificate successfully created')
    success_url = reverse_lazy('certificates')
    extra_context = {'title': _('Create certificate'),
                     'btn_name': _('Create')
                     }

    def get_form(self):
        form = super().get_form()
        form.fields["start_date"].widget = DatePickerInput()
        form.fields["finish_date"].widget = DatePickerInput()
        return form


class UpdateCertificate(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = Certificate
    fields = ['number']
    template_name = "certificates/form.html"
    success_message = _('Certificate successfully updated')
    success_url = reverse_lazy('certificates')
    extra_context = {'title': _('Update certificate'),
                     'btn_name': _('Update'),
                     }


class DeleteCertificate(SuccessMessageMixin, AppLoginRequiredMixin, DeleteView):
    model = Certificate
    template_name = "certificates/delete.html"
    context_object_name = "certificate"
    success_message = _('Certificate successfully deleted')
    success_url = reverse_lazy('certificates')
    extra_context = {'title': _('Delete certificate'),
                     'btn_name': _('Yes, delete'),
                     }

    def post(self, request, *args, **kwargs):
        if self.get_object().users.count():
            messages.error(
                self.request,
                _('It`s not possible to delete the certificate '
                  'that is belong to user')
            )
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
