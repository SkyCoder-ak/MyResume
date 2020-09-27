from django import forms
from phonenumber_field.formfields import PhoneNumberField

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid phone number (e.g. +918888888888).'
}

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    com_name = forms.CharField(max_length=60)
    com_add = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = PhoneNumberField(error_messages=my_default_errors)
    message = forms.CharField(widget=forms.Textarea)