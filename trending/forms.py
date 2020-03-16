from django import forms
from .models import Post, Comment




class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 5, 'rows': 3}))
    class Meta:
        model = Post
        fields = ['title', 'sub_title', 'content', 'image']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Comment' , widget=forms.Textarea(attrs={'cols': 5, 'rows': 3}))
    class Meta:
        model = Comment
        fields = ['content']
