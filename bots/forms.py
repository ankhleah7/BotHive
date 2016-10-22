from django import forms

from bots.models import Printer_Type
from bots.models import Pod

#ask what needs to live here and why Printer_type and pod don't accept
class Printer_TypeForm(forms.ModelForm):
    class Meta:
        model = Printer_Type
        fields  = ['serial', 'plastic' , 'series' ]



"""import the model you want to use from your models. use (form.Forms):
use class MEta: indicate your model. then select the fields which is the text promt
that allows them to place things into your list. classes are made in models and imported into views.
forms follow the class___(form.FORMS):
class Meta: model = the class your using, fields = list with option ['']"""
