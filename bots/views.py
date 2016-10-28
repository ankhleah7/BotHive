from django.http import HttpResponse
from django.shortcuts import render

from bots.forms import Printer_TypeForm
from bots.models import Printer_Type
from bots.models import Pod


# S = serial_number
# B = bot_type
# I = ip address


def index(request):
    if request.method == 'POST':
        # Need a form to import before it can be called
        form = Printer_TypeForm(request. POST)
        if form.is_valid():
            form.save()
    return HttpResponse("bots are ready to be assigned.")

#http://localhost:8000/bots/printerinput/

def printer_input(request):
    if request.method == 'POST':
        printer_form = Printer_TypeForm(request.POST)
        if printer_form.is_valid():

            printer_form.save()

    else:
        printer_form = Printer_TypeForm()
    context = {'printer_form': printer_form,}

    return render(request, 'printerinput.html' , context)

"""
this still uses classes but they don't have to come from the models.
the same class function . making a class
then desgining a meta, then defining a mdel and fields.
 """

def pod_order(request):
    """
    This view should display how this individual pod grabs printers from the database and
    saves it in a dictionary that can be edited.
    :param request:
    :return:
    """
    heading = 'Create a Pod of Printers'

    if request.method == 'POST':
        pod_order_form = pod_form(request.POST)
        if pod_order_form is valid:
            pod_order_form.save

    else:
        pod_form = pod_order_form()
    context = {'pod_form': pod_form,}

    return render(request, 'podinput.html' , context)