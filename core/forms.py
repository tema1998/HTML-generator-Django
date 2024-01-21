from django import forms

from core.models import Result, Header, Footer


class NameForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('name',)
