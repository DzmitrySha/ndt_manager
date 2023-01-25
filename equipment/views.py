from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView, ListView,
                                  )
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _
from equipment.models import Equipment
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
    template_name = 'eq_detail.html'
    pass


class CreateEquipment(CreateView):
    model = Equipment
    pass


class UpdateEquipment(UpdateView):
    model = Equipment
    pass


class DeleteEquipment(DeleteView):
    model = Equipment
    pass
