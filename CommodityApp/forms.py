from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User

class DateInput(forms.DateInput):
    input_type = "date"

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    last_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    username = forms.CharField(max_length=254,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def clean(self):
        cleaned_data = super(UserCreationForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class FarmerForm(forms.ModelForm):
    address = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    city = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    state = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = Farmer
        fields = ('address','city','state',)


class ManufacturerForm(forms.ModelForm):
    company_name = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    company_add = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    address = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    city = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    state = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = Manufacturer
        fields = ('company_name','company_add','address','city','state', )


class CustomerForm(forms.ModelForm):
    address = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    city = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    state = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
        model = Customer
        fields = ('address','city','state',)

class UserTypeForm(forms.Form):
    FARMER = 'FR'
    RETAIL_BUYER = 'RB'
    MANUFACTURER = 'MR'
    TRUCKDRIVERS = 'TD'
    DELIVERYBOY = 'DB'
    COURIERCOMPANY = 'CC'
    USER_CHOICES = (
        (FARMER,'Farmer'),
        (RETAIL_BUYER,'Retail buyer'),
        (MANUFACTURER,'Manufacturer'),
        (TRUCKDRIVERS,'Truck Drivers'),
        (DELIVERYBOY,'Delivery Boy'),
        (COURIERCOMPANY,'Courier Company'),
    )
    usertype= forms.CharField(max_length=30,widget=forms.Select(choices=USER_CHOICES,attrs={'class':'d-form form-control'}))

class CommodityForm(forms.Form):
    name = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    amount = forms.FloatField( widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.01",'class':'form-control'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'d-form form-control'}))
    breed=forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'d-form form-control'}))
    priceperkg = forms.FloatField(widget= forms.TextInput(attrs={'class':'d-form form-control'}))
    priceperquintal = forms.FloatField(widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.01",'class':'form-control'}))
    type_choices = (
        ('FRUIT','Fruit'),
        ('VEGIES','Vegetables'),
        ('PULSES','Pulses'),
        ('CEREAL','Cereal'),
        ('OTHERS','Others')
    )
    type = forms.CharField(max_length=100,widget=forms.Select(choices=type_choices,attrs={'class':'d-form form-control'}))
    perishable = forms.BooleanField()
    # date = forms.DateField(widget=DateInput)
    image = forms.ImageField(widget= forms.FileInput(attrs={'class':'form-control'}))

    class Meta:
        Model = Commodities
        fields = {'name','amount','breed','priceperkg','priceperquintal','image'}

class Search(forms.Form):
    search = forms.CharField(max_length=200)

class FeedbackForm(forms.Form):
    rating = forms.FloatField(max_value=5, min_value=0, widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "0.01",'class':'form-control'}))
    desc = forms.CharField(max_length=200,widget= forms.TextInput(attrs={'class':'d-form form-control'}))

    class Meta:
        Model = Ratings
        fields={'rating','desc'}
