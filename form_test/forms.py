from .models import RegisterModel, PriorHealthPlanModel, ConsentDateModel
from django import forms


class DateField(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class TelephoneField(forms.TextInput):
    input_type = "tel"


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_of_birth"].widget = DateField()
        self.fields["phone_number"].widget = TelephoneField()
        self.fields["address"].widget = forms.Textarea()


class PriorHealthPlanForm(forms.ModelForm):
    class Meta:
        model = PriorHealthPlanModel
        fields = "__all__"


class ConsentDateForm(forms.ModelForm):
    class Meta:
        model = ConsentDateModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date"].widget = DateField()
