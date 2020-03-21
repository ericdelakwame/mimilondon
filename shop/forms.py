from django import forms
from .models import (
    Category, SubCategory, Product, Color, Size, Options
)



class CategoryForm(forms.ModelForm):
    name = forms.ChoiceField(choices=(
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Children', 'Children'),
        ('Accessories', 'Accessories'),
        
      
    ), widget=forms.RadioSelect())
    
    class Meta:
        model = Category
        fields = ['name']


class SubCategoryForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = ['name']


class ProductForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), widget=forms.RadioSelect(), initial=0, required=False)
    color = forms.ModelChoiceField(queryset=Color.objects.all(), widget=forms.RadioSelect(), initial=0, required=False)
    available = forms.ChoiceField(choices=(
        ('True', 'True'),
        ('False', 'False'),
    ),
        widget=forms.RadioSelect()
    )
    class Meta:
        model = Product
        exclude = [
            'slug',  'created', 'updated', 'sub_category', 'available'
        ]
    


class SizeForm(forms.ModelForm):
 
    class Meta:
        model = Size
        fields = ['size']

    
    def __init__(self, product, *args, **kwargs):
        super(SizeForm, self).__init__(*args, **kwargs)
        self.fields['size']=forms.ModelChoiceField(queryset=product.sizes, widget=forms.Select(), required=False)
    

    
    



class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['color']
    
    def __init__(self, product, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)
        self.fields['color'] = forms.ModelChoiceField(queryset=product.colors, widget=forms.Select(), required=False)
   
        
    



class ProductColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['color']


class ProductSizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['size']

class OptionsForm(forms.ModelForm):

    
    class Meta:
        model = Options
        fields = ['size', 'color']

    
    def __init__(self, product, *args, **kwargs):
        super(OptionsForm, self).__init__(*args, **kwargs)
        self.fields['size']=forms.ModelChoiceField(queryset=product.sizes, widget=forms.Select())
        self.fields['color'] = forms.ModelChoiceField(queryset=product.colors, widget=forms.Select())

    
