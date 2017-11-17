# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):

	Patient_ID = models.CharField(("Patient_ID"), max_length = 55, null = True, blank = True)
	Patient_Name = models.CharField(("Patient_Name"), max_length = 40, null = True, blank = True)
	Gender = models.CharField(("Gender(F or M)"), max_length = 1 )
	Home_Address = models.CharField(("Home_Address"), max_length = 100, null = True, blank = True )
	Date_Of_Birth = models.DateField(("Date_Of_Birth"))
	Doctor_ID = models.CharField(("Doctor_ID"), max_length = 55)
	Contact = models.CharField(("Contact"), max_length = 55)
	Email = models.EmailField(("Email"), max_length = 100, null = True, blank = True)

	class Meta:
		verbose_name = 'PATIENT'
		verbose_name_plural = 'PATIENTS'

	def __unicode__(self):
		return self.Patient_ID
