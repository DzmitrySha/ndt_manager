import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Report(models.Model):
    NDT_REPORT = _('NDT')
    TD_REPORT = _('TD')

    REPORT_TYPE_CHOICES = [
        (NDT_REPORT, _('NDT')),
        (TD_REPORT, _('TD')),
    ]
    year = datetime.date.today().year

    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    updated_at = models.DateTimeField(verbose_name=_("Updated date"),
                                      auto_now=True)
    report_num = models.CharField(max_length=10, unique=True,
                                  default=f"01-{year}",
                                  verbose_name=_('Report number'))
    report_date = models.DateField(verbose_name=_('Report date'),
                                   default=timezone.now)
    report_type = models.CharField(max_length=12, choices=REPORT_TYPE_CHOICES,
                                   default=NDT_REPORT,
                                   verbose_name=_('Report type'))
    station = models.ForeignKey(to='stations.Station', on_delete=models.PROTECT,
                                verbose_name=_('Station'))
    equipment = models.ForeignKey(
        to='equipment.Equipment', on_delete=models.PROTECT,
        related_name='equipment', verbose_name=_('Equipment'))

    parts_names = models.CharField(max_length=120, blank=True,
                                   verbose_name=_('Parts names'))

    description = models.TextField(verbose_name=_('Description'), blank=True)

    file = models.FileField(upload_to='reports/uploads/%Y-%m-%d/', blank=True)

    def __str__(self):
        return f"""{_('Report')} {self.report_num} at {self.report_date}
         {self.equipment.equipment_type} {self.equipment.name},
         {self.equipment.station}"""
