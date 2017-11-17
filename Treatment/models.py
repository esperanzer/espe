# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Treatment(models.Model):

	Treatment_ID = models.CharField(("Treatment_ID"), max_length = 55)
	Patient_Name = models.CharField(("Patient_Name"), max_length = 55, null = True, blank = True)
	Diagnosis = models.CharField(("Diagnosis"), max_length = 100, null = True)
	Patient_ID = models.CharField(("Patient_ID"), max_length = 55)
	Disease  = models.CharField(("Disease"), max_length = 100, null = True, blank = True)
	Date_Of_Treatment = models.DateField(("Date _Of_Appointment"))
	Details = models.CharField(("Details"), max_length = 100, null = True, blank = True)

	class Meta:
		verbose_name = 'TREATMENT'
		verbose_name_plural = 'TREATMENTS'
	def __unicode__(self):
		return self.Treatment_ID
