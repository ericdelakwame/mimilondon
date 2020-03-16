from django import forms
from .models import Order, OrderItem
from accounts.models import Customer
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from django.contrib.gis.forms import PointField
from django.contrib.gis.forms.widgets import OSMWidget
from leaflet.forms.widgets import LeafletWidget


class OrderCreateForm(forms.ModelForm):
    point = PointField(label='Location', widget=LeafletWidget(attrs={
        'default_center': (5.56, 0.22),
    }), required=False)
    tel_no = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(attrs={'placeholder': (u'Your Tel Number:')}),
        label=(u'Country Code'),
        required=False,
        initial='+233'
    )
    preferred_delivery_date = forms.DateField(required=False)

    class Meta:
        model = Order
        fields = [
            'first_name', 'last_name', 'email',
            'address', 'city', 'tel_no', 'country', 'preferred_delivery_date', 'point',
        ]

   