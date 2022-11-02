from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class reviewForm(forms.Form):
    review = forms.CharField(label="review", max_length=256, min_length=1)
    rate = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])