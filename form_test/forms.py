from .models import TestModel
from django import forms


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = "__all__"
