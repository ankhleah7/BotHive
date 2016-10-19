from django import forms

from BotHive.models import Printer_Type
from BotHive.models import Pod

#ask what needs to live here and why Printer_type and pod don't accept
class Printer_TypeForm(forms.ModelForm):
    class Meta:
        model = 'printer_name'
        fields = ['printer type', 'plastic color' ]
