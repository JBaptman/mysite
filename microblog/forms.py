# encoding: utf-8
from django import forms
from .models import Message


class PostForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'required': 'True',
                'placeholder': 'Say something...'
            })
        }