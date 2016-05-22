from django.forms import ModelForm
from hello_world_app.models import Name


class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = ['value']
