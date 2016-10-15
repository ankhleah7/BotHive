from django import forms

from BotHive.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stuff', 'rating', ]
