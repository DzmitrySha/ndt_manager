from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NDTManagerConfig(AppConfig):
    name = 'ndt_manager'
    verbose_name = _('NDT Manager')
