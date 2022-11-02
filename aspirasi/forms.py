from django import forms
<<<<<<< HEAD:perpustakaan/forms.py
from django.core.validators import MinValueValidator, MaxValueValidator


class reviewForm(forms.Form):
    review = forms.CharField(label="review", max_length=256, min_length=1)
    rate = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
=======
from .models import Aspirasi

class AspirasiForm(forms.ModelForm):
    class Meta:
        model = Aspirasi
        exclude = ('user', )
>>>>>>> 20cca0dcf0a46c8bc1fa9424f3d724a97f2058d4:aspirasi/forms.py
