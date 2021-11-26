from django import forms
from django.forms import widgets
from models import *
from myapi.models import *
from phonenumber_field.formfields import PhoneNumberField

class PersonForm(forms.ModelForm):
    phoneNumber = PhoneNumberField()
    class Meta:
        model=Person
        widgets {
            'passwd': forms.PasswordInput(),
        }

