from django import forms
from .models import UrlLink

class PostUrl (forms.ModelForm):
    class Meta:
        model=UrlLink
        fields=('website',)
        # fields=('website',)
