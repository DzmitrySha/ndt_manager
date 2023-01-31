from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Station(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Name'), unique=True)
    created_date = models.DateTimeField(verbose_name=_("Created date"),
                                        default=timezone.now)
    address = models.CharField(max_length=120, verbose_name=_('Address'),
                               default='', blank=True)

    def __str__(self):
        return self.name
