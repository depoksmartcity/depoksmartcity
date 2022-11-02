from django import forms
from .models import Aspirasi

class AspirasiForm(forms.ModelForm):
    class Meta:
        model = Aspirasi
        exclude = ('user', )