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


# def random_stuff_in_a_function():
#     list1 = ['Bot-Type', 'Serial Number' , 'IP Address' , 'Desired CLuster Location']
#     Bot_Type = ['Taz 6' , 'Taz 5', 'Mini' , 'NinjaFLex Mini'],
#     Serial_Number = [raw_input()],
#     ip_Adress = [raw_input()]
#
#     for bot in Bot_Type:
#         print "Select a printer",
#         #bot.save,
#
#     for ser in Serial_Number:
#         print "insert ip adress", [raw_input()],
#         #ser.save,
#
#     for ip in ip_Adress:
#         print "ip address:" , [raw_input()],
#http://localhost:8000/bots/printerinput/

def printer_input(request):
    if request.method == 'POST':
        printer_form = Printer_TypeForm(request.POST)
        if printer_form.is_valid():
            print 'Hello World'

            printer_form.save()

    else:
        printer_form = Printer_TypeForm()
    context = {'printer_form': printer_form,}

    return render(request, 'printerinput.html' , context)
    #return HttpResponse("bots are ready to be assigned.")
        #ip.save,
#def index(request):
#    if request.mthod == 'POST':
#      :  form =
"""this still uses classes but they don't have to come from the models.
the same class function . making a class
then desgining a meta, then defining a mdel and fields. """