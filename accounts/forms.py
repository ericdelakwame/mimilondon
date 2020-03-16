from django import forms
from django.contrib.auth.forms import (
    UserChangeForm, UserCreationForm

)

from .models import (
    User, Customer, Staff, Admin
)


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class CustomerForm(UserCreationForm):
    tel_no = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': (u'Your Tel Number:')}),
        label=(u'Country Code'),
        required=False,
        initial='+44'
    )

    class Meta:
        model = Customer
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'tel_no',
            'gender',
            'photo',
            'address',
            'city',
            'country',
            'password1'
        ]
    
    


class StaffForm(UserCreationForm):
    tel_no = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': (u'Your Tel Number:')}),
        label=(u'Country Code'),
        required=False,
        initial='+44'
    )

    class Meta:
        model = Staff
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'tel_no',
            'photo',
            'address',
            'city',
            'country',
            'password1'
        ]


class AdminForm(UserCreationForm):
    tel_no = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': (u'Your Tel Number:')}),
        label=(u'Country Code'),
        required=False,
        initial='+44'
    )

    class Meta:
        model = Admin
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'tel_no',
            'photo',
            'address',
            'city',
            'country',
            'password1'
        ]
