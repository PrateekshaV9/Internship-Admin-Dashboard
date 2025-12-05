from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order


class StaffRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']


class StaffOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity']
