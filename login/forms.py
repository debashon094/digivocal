from django import forms
from .models import Login


class ListForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = {"username", "password", "checked"}
