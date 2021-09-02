from .models import RegisterModel, PriorHealthPlanModel, ConsentDateModel
from django import forms


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = "__all__"


class PriorHealthPlanForm(forms.ModelForm):
    class Meta:
        model = PriorHealthPlanModel
        fields = "__all__"


class ConsentDateForm(forms.ModelForm):
    class Meta:
        model = ConsentDateModel
        fields = "__all__"
