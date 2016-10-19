from django import forms

#ask what to do here
from BotHive.models import Printer_Type



class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stuff', 'rating', ]
