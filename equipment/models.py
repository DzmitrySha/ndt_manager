from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Equipment(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name/model'),
                            blank=False, unique=True)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_at = models.DateTimeField(verbose_name=_("Created date"),
                                      default=timezone.now)
    updated_at = models.DateTimeField(verbose_name=_("Updated date"),
                                      auto_now=True)
    station_num = models.CharField(
        verbose_name=_('Station number'), max_length=4, blank=True)
    factory_num = models.CharField(
        verbose_name=_('Factory number'), max_length=12, blank=True)
    inventory_num = models.CharField(
        verbose_name=_('Inventory number'), max_length=12, blank=True)
    register_num = models.CharField(
        verbose_name=_('Registration number'), max_length=16, blank=True,
        unique=True)
    start_op_date = models.DateField(
        verbose_name=_("Start operation date"),
        default=timezone.now, blank=True)
    op_time = models.IntegerField(
        verbose_name=_('Total operation time'), blank=True)
    last_repair_date = models.DateField(
        verbose_name=_("Last repair date"), default=timezone.now, blank=True)
    op_time_after_repairs = models.IntegerField(
        verbose_name=_('Operation time after major repairs'), blank=True)
    equipment_type = models.ForeignKey(
        to='equiptypes.EquipType', on_delete=models.PROTECT, blank=False,
        related_name='equiptypes', verbose_name=_('Equipment type'))
    station = models.ForeignKey(
        to='stations.Station', on_delete=models.PROTECT, blank=False,
        related_name='stations', verbose_name=_('Station'), default='')

    def __str__(self):
        return f"{self.equipment_type} {self.name}, " \
               f"{_('ст.№')}{self.station_num}"

    # labels = models.ManyToManyField(
    #     'labels.TaskLabels', through='Relations',
    #     through_fields=('task', 'label'), blank=True,
    #     related_name='labels', verbose_name=_('Labels'),
    # )

# class Relations(models.Model):
#     task = models.ForeignKey(to='tasks.Task', on_delete=models.CASCADE)
#     label = models.ForeignKey(to='labels.TaskLabels',
#     on_delete=models.PROTECT)
