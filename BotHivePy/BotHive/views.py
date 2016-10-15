from django.http import HttpResponse
from django.shortcuts import render

from BotHive.forms import RatingForm
from BotHive.models import PRINTER_TYPES,


# S = serial_number
# B = bot_type
# I = ip address
#from
#from django.shortcuts import render

#from django.http impofrontend


# from BotHive.models import Cluster
# from BotHive.models import Pods

def index(request):
    if request.method == 'POST':
        form = Bot_Type(request. POST)
        if form.is_valid():
            form.save
    return HttpResponse("bots are ready to be assigned.")

list1 = ['Bot-Type', 'Serial Number' , 'IP Address' , 'Desired CLuster Location']
Bot_Type = ['Taz 6' , 'Taz 5', 'Mini' , 'NinjaFLex Mini'],
Serial_Number = [raw_input()],
ip_Adress = [raw_input()]

for bot in Bot_Type:
    print "Select a printer",
    #bot.save,

for ser in Serial_Number:
    print "insert ip adress", [raw_input()],
    #ser.save,

for ip in ip_Adress:
    print "ip address:" , [raw_input()],
    #ip.save,

#def index(request):
#    if request.mthod == 'POST':
#        form =
