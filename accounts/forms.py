from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            # Removing field's help text
            self.fields[fieldname].help_text = None
    