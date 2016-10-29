from __future__ import unicode_literals

from django.db import models
import string

#printer types, plastic type, serial number, number in a pod, number of pods in cluster
list1 = (('1', 'Mini'), ('2' , 'Taz 5'), ('3', 'Taz 6'), ('4', 'NinjaFlex Mini'))
list2 = (('1', 'Black ABS'), ('2', 'Green ABS'), ('3', 'Silver ABS'),
         ('4', 'Black NinjaFlex'), ('5', 'Green NinjaFlex'),
         ('6', 'Pink NGen Test'))
list3 = (('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'), ('5', 'E'), ('6', 'F'),
         ('7', 'G'), ('8', 'H'), ('9', 'I'), ('10', 'J'), ('11', 'K'), ('12', 'L'),
         ('13', 'M'), ('14', 'N'), ('15', 'O'), ('16', 'P'), ('17', 'Q'), ('18', 'R'),
         ('19', 'S'), ('20', 'T'), ('21', 'U'), ('22', 'V'), ('23', 'W'), ('24', 'X'),
         ('25', 'Y'), ('26', 'Z'))
CHAR_CHOICES = [(letter, letter) for letter
        in string.ascii_uppercase]
# alt_list3 =list(string.ascii_uppercase)

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
            #dict(list1).get[self.series], self.serial, dict(list2).get[self.plastic]')'
    #def select_printer(self):
    #look for the function of unique = TRUE
    #

class Pod(models.Model):
    #pod has a letter value, then the number of printers, specific printers, plastic type
    #pod_id = models.CharField(default='A', choices=list3, max_length=1) this broke
    #pod_id = [(letter, letter) for letter in string.ascii_uppercase] this broke
    pod_id = models.CharField(default='A', choices=CHAR_CHOICES, max_length=1)
    count = models.IntegerField(default = 1)
    printer_type = models.ForeignKey(Printer_Type)


    def __unicode__(self):
        return 'Pod -- {} -- {} -- {}'.format(
            self.pod_id, self.count, self.printer_type
        )

class Cluster(models.Model):
    """gather all the pods with all the printers together into a large group."""
    pod_hierarchy = models.ForeignKey(Pod)
    printer_hierarchy = models.ForeignKey(Printer_Type)
    cluster_count = models.IntegerField(default = 1)

    def __unicode__(self):
        return 'Cluster -- {} -- {} --{}'.format(
            self.pod_hierarchy, self.pod_hierarchy, self.cluster_count
        )