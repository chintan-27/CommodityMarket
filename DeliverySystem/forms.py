from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *

class CForm(forms.Form):
    SUPERFAST = 'SF'
    NORMAL = 'NL'
    DELIVERY_CHOICES = (
        (SUPERFAST,'SUPERFAST'),
        (NORMAL,'NORMAL'),
    )
    usertype= forms.CharField(max_length=30,widget=forms.Select(choices=DELIVERY_CHOICES,attrs={'class':'d-form form-control'}))
    deliveryChargePerKg = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'d-form form-control'}))

    class Meta:
         model = Courier
         fields = {'usertype','deliveryChargePerKg'}

class TForm(forms.Form):
    TRUCK_TYPE = (
        ('AC','AIR CONDITIONED'),
        ('NL','NORMAL'),
    )
    trucktype= forms.CharField(max_length=30,widget=forms.Select(choices=TRUCK_TYPE,attrs={'class':'d-form form-control'}))
    STATUS_TYPE = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),
    ('Busy','Busy'),
    )
    status= forms.CharField(max_length=30,widget=forms.Select(choices=STATUS_TYPE,attrs={'class':'d-form form-control'}))
    city= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
         model = TruckDrivers
         fields = {'trucktype','status','city'}

class DForm(forms.Form):
    STATUS_TYPE = (
    ('Available','Available'),
    ('Unavailable','Unavailable'),
    ('Busy','Busy'),
    )
    status= forms.CharField(max_length=30,widget=forms.Select(choices=STATUS_TYPE,attrs={'class':'d-form form-control'}))
    city= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
         model = DeliveryBoy
         fields = {'status','city'}
