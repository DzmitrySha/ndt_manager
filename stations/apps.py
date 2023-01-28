from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stations'
    verbose_name = _('Stations')
