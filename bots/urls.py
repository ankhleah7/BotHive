from django.conf.urls import url

from bots import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^printerinput/' , views.printer_input),
    url(r'^podinput/' , views.Pod)
]
