from django import forms
from .models import (
    Category, SubCategory, Product, Color, Size
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
    

class ColorForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['color']


class SizeForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['size']



class ColorForm(forms.ModelForm):
    size = forms.ModelMultipleChoiceField(queryset=Color.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Color
        fields = ['color']



class ProductColorForm(forms.ModelForm):
    color = forms.ModelChoiceField(queryset=Color.objects.all(), required=False, widget=forms.RadioSelect())
    class Meta:
        model = Color
        fields = ['color']


class ProductSizeForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), required=False, widget=forms.RadioSelect())

    class Meta:
        model = Size
        fields = ['size']
