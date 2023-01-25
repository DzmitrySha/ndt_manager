from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class UserCreationFormCustom(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].help_text = _("Enter user first name.")
        self.fields['last_name'].help_text = _("Enter user last name.")

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']
