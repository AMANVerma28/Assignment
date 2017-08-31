# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmerinfo(models.Model):
	farmer_id = models.IntegerField();
	farmer_name = models.CharField(max_length=30)
	farmer_village = models.CharField(max_length=25)
	farmer_farms = models.IntegerField()

	def __str__(self):
		return "%s" %(self.farmer_id)

#	class Meta:
#		ordering = ('created',)