
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import TravelInfo, Vehicle, Payment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TravelForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    phoneNo = forms.IntegerField()
    boarding = forms.CharField()
    destination = forms.CharField()
    date = forms.DateTimeField()

    class Meta:
        model = TravelInfo
        fields = ['name', 'email', 'phoneNo', 'boarding', 'destination', 'date']

class VehicleForm(ModelForm):
    name = forms.CharField()

    class Meta:
        model = Vehicle
        fields = ['name']



class PaymentForm(ModelForm):
    Pname = forms.CharField()
    cardName = forms.CharField()
    cardNumber = forms.IntegerField()
    ExpDate = forms.DateField()
    cvv = forms.IntegerField()

    class Meta:
        model = Payment
        fields = ['Pname', 'cardName', 'cardNumber', 'ExpDate', 'cvv']
