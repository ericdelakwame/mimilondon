from django import forms
from shop.models import Product, Color, Size




class NewProductForm(forms.ModelForm):
    colors = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), initial=0, required=False, widget=forms.CheckboxSelectMultiple())
    sizes = forms.ModelMultipleChoiceField(queryset=Size.objects.all(), initial=0, required=False, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Product
        exclude = [
            'sub_category',
            'slug',
            'created',
            'updated',
            'size',
            'color',
        ]