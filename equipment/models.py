from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import get_user_model


class Equipment(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Name/model'),
                            blank=False)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    updated_date = models.DateTimeField(verbose_name=_("Updated date"),
                                        auto_now=True)
    # equipment_type = models.ForeignKey(...)

    station_num = models.CharField(
        verbose_name=_('Station number'), max_length=2, blank=True)
    factory_num = models.CharField(
        verbose_name=_('Factory number'), max_length=20, blank=True)
    inventory_num = models.CharField(
        verbose_name=_('Inventory number'), max_length=20, blank=True)
    register_num = models.CharField(
        verbose_name=_('Registration number'), max_length=20, blank=True)
    start_op_date = models.DateField(
        verbose_name=_("Start operation date"),
        default=timezone.now, blank=True)
    op_time = models.IntegerField(
        verbose_name=_('Total operation time'), blank=True)

    last_repair_date = models.DateTimeField(
        verbose_name=_("Last repair date"), default=timezone.now, blank=True)
    op_time_after_repairs = models.IntegerField(
        verbose_name=_('Operation time after major repairs'), blank=True)

    # executor = models.ForeignKey(
    #     to=get_user_model(), on_delete=models.CASCADE, blank=True, null=True,
    #     default='', related_name='executors', verbose_name=_('Executor'),
    # )
    # author = models.ForeignKey(
    #     to=get_user_model(), on_delete=models.PROTECT, blank=False,
    #     related_name='authors', verbose_name=_('Author'),
    # )
    # status = models.ForeignKey(
    #     to='statuses.TaskStatus', on_delete=models.PROTECT, blank=False,
    #     related_name='statuses', verbose_name=_('Status'),
    # )
    # labels = models.ManyToManyField(
    #     'labels.TaskLabels', through='Relations',
    #     through_fields=('task', 'label'), blank=True,
    #     related_name='labels', verbose_name=_('Labels'),
    # )

    def __str__(self):
        return self.name


# class Relations(models.Model):
#     task = models.ForeignKey(to='tasks.Task', on_delete=models.CASCADE)
#     label = models.ForeignKey(to='labels.TaskLabels',
#     on_delete=models.PROTECT)
