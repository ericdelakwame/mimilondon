from django import forms
from .models import HomeVideo




class HomeVideoForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 3, 'rows':3,
    }))
    class Meta:
        model = HomeVideo
        fields = ['vid', 'content']