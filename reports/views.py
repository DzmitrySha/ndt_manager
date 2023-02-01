from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from reports.forms import ReportForm
from reports.models import Report
from ndt_manager.mixins import AppLoginRequiredMixin


class ReportsList(AppLoginRequiredMixin, ListView):
    model = Report
    template_name = "reports/reports.html"
    context_object_name = "reports"
    extra_context = {'title': _('Reports'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateReport(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = "reports/form.html"
    success_message = _('Report successfully created')
    success_url = reverse_lazy('reports')
    extra_context = {'title': _('Create report'),
                     'btn_name': _('Create')
                     }

    def get_form(self):
        form = super().get_form()
        form.fields["report_date"].widget = DatePickerInput()
        return form


class UpdateReport(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = Report
    form_class = ReportForm
    template_name = "reports/form.html"
    success_message = _('Report successfully updated')
    success_url = reverse_lazy('reports')
    extra_context = {'title': _('Update report'),
                     'btn_name': _('Update'),
                     }


class DeleteReport(SuccessMessageMixin, AppLoginRequiredMixin, DeleteView):
    model = Report
    template_name = "reports/delete.html"
    success_url = reverse_lazy('reports')
    success_message = _('Report successfully deleted')
    context_object_name = "report"
    extra_context = {'title': _('Delete report'),
                     'btn_name': _('Yes, delete'),
                     }

    def post(self, request, *args, **kwargs):
        if self.get_object().reports.count():
            messages.error(
                self.request,
                _('It`s not possible to delete the report that is being used')
            )
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
