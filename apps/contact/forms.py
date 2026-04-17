from django import forms
from apps.contact.models import ContactMessage
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django_recaptcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(
        required=False,
        widget=forms.HiddenInput(attrs={"autocomplete": "off"}),
        label=""
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox()
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Your message",
            }),
        }
