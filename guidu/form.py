from django import forms
from models import Guidu


class FormGuidu(forms.ModelForm):
    class Meta:
        model = Guidu
        fields = ('nome', 'idade')

