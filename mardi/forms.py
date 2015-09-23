from django import forms
from django.forms import ModelForm


class contactForm(forms.Form):
    name = forms.CharField(label="Name")
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField(label="Email")
    message = forms.CharField(label="Your Query",widget=forms.Textarea)
