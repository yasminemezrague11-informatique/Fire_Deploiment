from django import forms
from .models import FireIncident
from .models import Citoyen

class FireIncidentForm(forms.ModelForm):
    class Meta:
        model = FireIncident
        fields = ['reporter_name', 'contact_number', 'address', 'fire_type', 'fire_severity']
        widgets = {
            'fire_description': forms.Textarea(attrs={'rows': 4}),
        }


class CitoyenForm(forms.ModelForm):
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label="Confirmez le mot de passe")

    class Meta:
        model = Citoyen
        fields = ['fullname', 'email', 'phone', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmPassword = cleaned_data.get("confirmPassword")

        if password != confirmPassword:
           raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        print(f"Password: {password}, ConfirmPassword: {confirmPassword}")  # Debug
        return cleaned_data
