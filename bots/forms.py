from django import forms

from bots.models import Printer_Type
from bots.models import Pod

#ask what needs to live here and why Printer_type and pod don't accept
class Printer_TypeForm(forms.ModelForm):
    class Meta:
        model = Printer_Type
        fields = ['serial', 'plastic' ]
