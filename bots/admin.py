from django.contrib import admin

from models import Printer_Type, Pod, Cluster

MyModels = [Printer_Type, Pod, Cluster]

admin.site.register(MyModels)

# Register your models here.
