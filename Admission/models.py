# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Admission(models.Model):
	
	Admission_ID = models.CharField(("Admission ID"), max_length = 55)
	Patient_ID = models.CharField(("Patient ID"), max_length = 55)
	Patient_Name = models.CharField(("Patient Name"), max_length = 55, null = True, blank = True)
	Treatment_ID = models.CharField(("Treatment ID"), max_length = 55, null = True, blank = True )
	Ward_ID = models.CharField(("Ward ID"), max_length = 55, null = True, blank = True)
	Details = models.CharField(("Details"), max_length = 255, null = True, blank = True)
	Date_Of_Admission = models.DateTimeField(("Date Time Field"))
	
	class Meta:

		verbose_name = 'ADMISSION'
		verbose_name_plural = 'ADMISSIONS'

	def __unicode__(self):
		return self.Details



