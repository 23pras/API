from django import forms
from django.db.models import fields
from django.forms import widgets
from models import *
from myapi.models import *
from phonenumber_field.formfields import PhoneNumberField

class PersonForm(forms.ModelForm):
    phoneNumber = PhoneNumberField()
    class Meta:
        model=Person
        fields = ('userId','FirstName','LastName','phoneNumber','Email','passwd')
        widgets = {
            'passwd': forms.PasswordInput(),
        }

