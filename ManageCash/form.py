from django import forms
from django.contrib.auth.forms import UserCreationForm
from ManageCash.models import *
from django.utils import timezone

class SignUp_Form(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'full_name', 'email', 'password1', 'password2']


class AddCash_Form(forms.ModelForm):
    class Meta:
        model = AddCash_Model
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'datetime': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                }
            ),
        }

class Expense_Form(forms.ModelForm):
    class Meta:
        model = Expense_Model
        fields = "__all__"
        exclude = ['user']
        widgets = {
            'datetime': forms.DateInput(
                format='Y-m-d',
                attrs={
                    'type': 'date',
                }
            ),
        }


