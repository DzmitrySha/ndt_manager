import django_filters
from reports.models import Report
# from stations.models import Station


class ReportsFilterForm(django_filters.FilterSet):
    report_date = django_filters.NumberFilter(
        field_name='report_date',
        lookup_expr='year')

    class Meta:
        model = Report
        fields = ['report_num', 'report_date', 'report_type',
                  'equipment']
