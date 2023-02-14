from django.contrib.auth.models import AbstractUser, models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    post = models.CharField(max_length=48, default='', blank=False,
                            verbose_name=_('Post'))

    def __str__(self):
        return self.get_full_name()
