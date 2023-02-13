from django.contrib.auth.models import AbstractUser, models


class User(AbstractUser):
    post = models.CharField(max_length=48, default='', blank=False)

    def __str__(self):
        return self.get_full_name()
