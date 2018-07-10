from django import forms
from .models import Restaurant
from django.contrib.auth.models import User
from django import forms



class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }
class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
       