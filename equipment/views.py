from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView,
                                  )
from django_filters.views import FilterView
from equipment.models import Equipment


class EquipmentList(FilterView):
    model = Equipment
    pass


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
