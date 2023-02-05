from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Certificate(models.Model):
    LEVEL_2 = _('2nd level')
    LEVEL_3 = _('3rd level')

    LEVEL_CHOICES = [
        (LEVEL_2, _('2nd level')),
        (LEVEL_3, _('3rd level')),
    ]

    VT = _('Visual testing method')
    UT = _('Ultrasonic testing method')
    PT = _('Penetrant testing method')
    MT = _('Magneting particle testing method')

    METHOD_CHOICES = [
        (VT, _('Visual testing method')),
        (UT, _('Ultrasonic testing method')),
        (PT, _('Penetrant testing method')),
        (MT, _('Magneting particle testing method')),
    ]

    created_at = models.DateTimeField(verbose_name=_("Created date"),
                                      default=timezone.now)
    number = models.CharField(max_length=32)
    method = models.CharField(max_length=32,
                              choices=METHOD_CHOICES, default=VT,
                              verbose_name=_('Method'))
    level = models.CharField(max_length=12,
                             choices=LEVEL_CHOICES, default=LEVEL_2,
                             verbose_name=_('Level'))
    start_date = models.DateField(
        verbose_name=_('Start date'), default=timezone.now)
    finish_date = models.DateField(
        verbose_name=_('Finish date'),
        default=timezone.now)
    owner = models.ForeignKey(to='users.User', on_delete=models.PROTECT,
                              blank=False)

    def __str__(self):
        return f"{self.number} {_('from')} {self.start_date}"
