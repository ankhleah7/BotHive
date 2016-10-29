from django.http import HttpResponse
from django.shortcuts import render

from bots.forms import Printer_TypeForm
from bots.models import Printer_Type
from bots.models import Pod


# S = serial_number
# B = bot_type
# I = ip address
""" if request.method == 'POST:
form = PodOrderForm(request.POST) form is a variable name which just needs to be consistent. keep in camal case
if form.is_valid(): keep this format
form.save()"""

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
    #http://localhost:8000/bots/podinput/
    """
    This view should display how this individual pod grabs printers from the database and
    saves it in a dictionary that can be edited.
    :param request:
    :return:
    """
    heading = 'Create a Pod of Printers'

    if request.method == 'POST':
        form = PodOrderForm(request.POST)
        if form.is_valid:
            form.save()

    else:
        form = PodOrderForm()
    context = {'pod_form': form,}

    return render(request, 'podinput.html' , context)


def cluster_order(request):

    #http://localhost:8000/bots/clusterinput/

    heading = 'Join Pods of Printers to The Cluster'

    if request.method == 'POST':
        form = ClusterOrder(request.POST)
        if form.is_valid():
            form.save()
    else:
        cluster_order = cluster_order_form()
    context = {'cluster_form': cluster_form,}

    return render(request, 'clusterinput.html', context)

