# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Ward(models.Model):
	Ward_ID = models.CharField(("Ward_ID"), max_length = 55)
	Patient_ID = models.CharField(("Patient_ID"), max_length = 55)
	Status = models.CharField(("Status"), max_length = 10, null = True, blank = True)

	class Meta:

		verbose_name ='WARD'
		verbose_name_plural = 'WARDS'

	def __unicode__(self):
		return self.Ward_ID