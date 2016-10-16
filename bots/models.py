from __future__ import unicode_literals

"""These pieces of info will be kept on a seperate dict that will store all these files and allow you to call them back."""
"""I need to figure out if i make a for loop statement at the end of each class or on the bottom and find a way to make a list that can be added to dynamically."""
"""Ask if looped statements need to be diefined in their class and then combined in lower code."""
"""Ask how to store these new lists and a way to call them later"""


from django.db import models


PRINTER_TYPES = ((1, 'mini'), (2 , 'Taz 5'), (3, 'Taz 6'), (4, 'NinjaFlex Mini'))

printer_name = models.CharField(max_length=50)
TAZ_5 = 'Taz 5'
TAZ_6 = 'Taz 6'
MINI = 'Mini'
FLEXY = 'Mini NinjaFLex'
BOT_TYPE_CHOICES = (
    (TAZ_6, 'Taz_6'),
    (TAZ_5, 'Taz_5'),
    (MINI, 'Mini'),
    (FLEXY, 'Mini_NinjaFlex')
)

class BotType(models.Model):
# This is the specific company model EX Lulxbot Taz 5, Taz 6, Mini, See Me CNC delta, etc.
    BotType = models.CharField( max_length= 10)
    cluster = models.ForeignKey('pods', on_delete=models.CASCADE,
        )


    #add a field printer bot to bot type
    #foreign key back to cluster
    #add the serial number and ip address to this class.

    # def __init__ (self, verbose_name=None, name=None, min_value=None, max_value=None,
    #     self.min_value, self.max_value = min_value, max_value
    #     models.IntegerField.__init__(self, verbose_name, name, **kwargs)


# class PrinterBot(models.Model):
#    Serial_number = models.CharField(max_length=50)
#
# #foreign key back to cluster
#
# class IpAddress(models.Model):
#     ip_address = models.CharField(max_length=20)
    def __unicode__(self):
        return 'BotHive - {} - {}'.format(self.title, self.ip_adress)


class Cluster (models.Model):
    """needs to generate a list, with questions of how large do you want a single cluster, give it a variable range for now of between 1 and 20 and allow you to name that cluster.
    Once cluster parameters are established the next question it asks is select the bots you wish to assign to each cluster; this will link to the previous bots page and allow you to select from that list, making a new list and saving said list."""


class Pods (models.Model):
    Pods = models.IntegerField(default=1, max_length=100)
    BotType = models.CharField(choices=BOT_TYPE_CHOICES)
    SerialNumber = models.IntegerField(default=1, max_length=100)
    #IP = models.IntegerField()

    def __unicode__(self):
        return 'pods -- {} -- {} -- {} -- {}'.format (self.BotType.pods, self.BotType, self.SerialNumber,
                                                      self.IP)

# add pods catagory here and populate it with the ability to define how many printers are in this pod
# Link bots page through many to many to jobs
# file field selects files on a desktop