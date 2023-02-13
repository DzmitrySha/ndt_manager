from django_filters import FilterSet
from equipment.models import Equipment


class EquipmentFilterForm(FilterSet):
    class Meta:
        model = Equipment
        fields = ['station', 'equipment_type']
