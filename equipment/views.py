from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView, ListView,
                                  )
from django.utils.translation import gettext_lazy as _
from equipment.models import Equipment
# from django_filters.views import FilterView
# from tasks.filters import TaskFilterForm


class EquipmentList(ListView):
    model = Equipment
    # filterset_class = TaskFilterForm
    template_name = "equipment/equipment.html"
    context_object_name = "equipment"
    extra_context = {'title': _('Equipment'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     'btn_show': _('Show'),
                     }


class EquipmentDetailView(DetailView):
    model = Equipment
    template_name = 'equipment/eq_detail.html'
    context_object_name = "equipment"
    extra_context = {'title': _('Equipment view'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateEquipment(SuccessMessageMixin, CreateView):
    model = Equipment
    fields = [
        'name', 'station_num', 'factory_num', 'inventory_num', 'register_num',
        'start_op_date', 'op_time', 'last_repair_date', 'op_time_after_repairs',
        'description',
    ]
    template_name = "equipment/form.html"
    success_message = _('Equipment successfully created')
    success_url = reverse_lazy('equipment')
    extra_context = {'title': _('Create equipment'),
                     'btn_name': _('Create')
                     }


class UpdateEquipment(UpdateView):
    model = Equipment
    fields = [
        'name', 'station_num', 'factory_num', 'inventory_num', 'register_num',
        'start_op_date', 'op_time', 'last_repair_date', 'op_time_after_repairs',
        'description',
    ]
    template_name = "equipment/form.html"
    success_message = _('Equipment successfully updated')
    success_url = reverse_lazy('equipment')
    extra_context = {'title': _('Update equipment'),
                     'btn_name': _('Update'),
                     }


class DeleteEquipment(DeleteView):
    model = Equipment
    template_name = "equipment/delete.html"
    context_object_name = "equipment"
    success_message = _('Equipment successfully deleted')
    success_url = reverse_lazy('equipment')
    extra_context = {'title': _('Delete equipment'),
                     'btn_name': _('Yes, delete'),
                     }
    # permission_required = 'equipment.author'
