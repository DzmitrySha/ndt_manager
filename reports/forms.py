from django import forms
from django.utils.translation import gettext_lazy as _
from django_select2 import forms as s2forms
from reports.models import Report
from stations.models import Station
from equipment.models import Equipment


class ReportCreateForm(forms.ModelForm):

    station = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        label=_("Station"),
    )

    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(),
        label=_("Equipment"),
        widget=s2forms.ModelSelect2Widget(
            queryset=Equipment.objects.all(),
            search_fields=['name__icontains'],
            dependent_fields={'station': 'station'},

        )
    )

    class Meta:
        model = Report
        fields = ['report_num', 'report_date', 'report_type', 'station',
                  'equipment', 'parts_names', 'description']
