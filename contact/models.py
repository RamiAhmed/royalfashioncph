from django.db import models
from django import forms

from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.

class ContactForm(forms.Form):
    sender_name = forms.CharField(required=False, max_length=200, label="Navn")
    sender_telephone = forms.CharField(max_length=8, label="Telefon Nummer (Kun danske numre)",
                                       validators=[
                                           RegexValidator(r'^\d{8}$', 'Kun tallene 0-9 er tilladte', 'Ugyldigt telefon nummer'),
                                           MinLengthValidator(8),
                                       ])
    sender = forms.EmailField(label="Email Addresse")
    cc_myself = forms.BooleanField(required=False, label="Send en kopi til min egen email", initial=True)
    subject = forms.CharField(max_length=100, label="Besked Emne")
    message = forms.CharField(widget=forms.Textarea, label="Besked Tekst")