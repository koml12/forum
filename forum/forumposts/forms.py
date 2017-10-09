from django import forms
from django.core import validators


class PostForm(forms.Form):
    text = forms.CharField()
    link = forms.URLField()


class CommentForm(forms.Form):
    text = forms.CharField()


