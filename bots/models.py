from __future__ import unicode_literals

"""These pieces of info will be kept on a seperate dict that will store all these files and allow you to call them back."""
"""I need to figure out if i make a for loop statement at the end of each class or on the bottom and find a way to make a list that can be added to dynamically."""
"""Ask if looped statements need to be diefined in their class and then combined in lower code."""
"""Ask how to store these new lists and a way to call them later"""


from django.db import models
import string



#ask about string.ascii
# printer types, plastic type, serial number, number in a pod, number of pods in cluster
list1 = (('1', 'Mini'), ('2' , 'Taz 5'), ('3', 'Taz 6'), ('4', 'NinjaFlex Mini'))
list2 = (('1', 'Black ABS'), ('2', 'Green ABS'), ('3', 'Silver ABS'),
         ('4', 'Black NinjaFlex'), ('5', 'Green NinjaFlex'),
         ('6', 'Pink NGen Test'))
list3 = (('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'),
         ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J'), ('k', 'K'), ('l', 'L'),
         ('m', 'M'), ('n', 'N'), ('o', 'O'), ('p', 'P'), ('q', 'Q'), ('r', 'R'),
         ('s', 'S'), ('t', 'T'), ('u', 'U'), ('v', 'V'), ('w', 'W'), ('x', 'X'),
         ('y', 'Y'), ('z', 'Z'))
# list4 =

class Printer_Type(models.Model):
    # This is the specific company model EX Lulxbot Taz 5, Taz 6, Mini, See Me CNC delta, etc
    series = models.CharField(default='Mini', choices=list1, max_length=100)
    serial = models.IntegerField(default=1)
    plastic = models.CharField(default='Black ABS', choices=list2, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return 'Pod -- {} -- {} -- {}'.format(
            dict(list1)[self.series], self.serial, dict(list2)[self.plastic])
            # dict(list1).get(self.series, ''), self.serial, dict(list3).get(self.plastic))
    #def select_printer(self):


class Pod(models.Model):
    #pod has a letter value, then the number of printers, specific printers, plastic type
    pod_id = models.CharField(default='A', choices=list3, max_length=1)
    count = models.IntegerField(default = 1)
    printer_type = models.ForeignKey(Printer_Type)

    def __unicode__(self):
        return 'Pod -- {} -- {} -- {}'.format(
            dict(list3).get(self.list(string.ascii_uppercase)), ''), self.count, self.printer_type


class Cluster (models.Model):
    # """needs to generate a list, with questions of how large do you want a single cluster, give it a variable range for now of between 1 and 20 and allow you to name that cluster.
    # Once cluster parameters are established the next question it asks is select the bots you wish to assign to each cluster; this will link to the previous bots page and allow you to select from that list, making a new list and saving said list."""

# Link bots page through many to many to jobs
# file field selects files on a desktop
    pass
