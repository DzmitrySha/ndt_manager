from django import forms
from django.utils.translation import gettext_lazy as _
# from django_select2.forms import ModelSelect2Widget
# from django_filters import widgets
from reports.models import Report
from stations.models import Station
from equipment.models import Equipment


class ReportForm(forms.ModelForm):

    station = forms.ModelChoiceField(
        queryset=Station.objects.all(),
        label=_("Station"),
        # widget=ModelSelect2Widget(
        #     model=Station,
        #     search_fields=['name__icontains'],
        #     dependent_fields={'station': 'station'},
        # )
    )

    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(),
        label=_("Equipment"),
        # widget=ModelSelect2Widget(
        #     model=Equipment,
        #     search_fields=['name__icontains'],
        #     dependent_fields={'station': 'station'},
        # )
    )

    class Meta:
        model = Report
        fields = ['report_num', 'report_date', 'report_type', 'station',
                  'equipment', 'parts_names', 'description']
