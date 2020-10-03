from django.forms import ModelForm
from django import forms
from .models import ContactForm,Comment

class Contact(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(widget=forms.Textarea)
    class Meta:
        model = ContactForm
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Text goes here!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
