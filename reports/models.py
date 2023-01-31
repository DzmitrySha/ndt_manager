from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Report(models.Model):
    NDT_REPORT = 'NDT'
    TD_REPORT = 'TD'

    REPORT_TYPE_CHOICES = [
        (NDT_REPORT, _('NDT Report')),
        (TD_REPORT, _('TD Report')),
    ]

    name = models.CharField(max_length=120, verbose_name=_('Report name'))
    report_type = models.CharField(max_length=12, choices=REPORT_TYPE_CHOICES,
                                   default=NDT_REPORT,
                                   verbose_name=_('Report type'))
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    updated_at = models.DateTimeField(verbose_name=_("Updated date"),
                                      auto_now=True)
    report_date = models.DateField(verbose_name=_('Report date'),
                                   default=created_date)
    report_num = models.CharField(max_length=10, unique=True,
                                  verbose_name=_('Report number'))
    equipment = models.ForeignKey(
        to='equipment.Equipment', on_delete=models.PROTECT, blank=False,
        related_name='equipment', verbose_name=_('Equipment'))
    description = models.TextField(verbose_name=_('Description'), blank=True)

    def __str__(self):
        return self.name
