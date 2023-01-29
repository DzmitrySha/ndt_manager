from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class EquipType(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Name'), default='')
    created_at = models.DateTimeField(verbose_name=_("Created date"),
                                      default=timezone.now)

    def __str__(self):
        return self.name
