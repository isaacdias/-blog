from django import forms
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Post
        fields = ['title', 'slug', 'image', 'body', 'author', 'status']


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)