from django import forms
from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(1, 21)
]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
    size = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)


    
    def __init__(self, product, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ModelChoiceField(queryset=product.sizes)
        self.fields['color'] = forms.ModelChoiceField(queryset=product.colors)
    
    


