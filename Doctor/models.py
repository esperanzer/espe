# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Doctor(models.Model):
	
	Doctor_ID = models.CharField(("Doctor ID"), max_length = 55, null = True, blank = True)
	Doctor_Name = models.CharField(("Doctor Name"), max_length = 55, null = True, blank = True)
	Password = models.CharField(("Password"),  max_length = 40)
	Gender = models.CharField(("Gender(F or M)"), max_length = 1) 
	Qualification = models.CharField(("Qualification"), max_length = 40, null = True, blank = True)
	Department = models.CharField(("Department"), max_length = 55, null = True, blank = True)
	Contact = models.CharField(("Contact"), max_length = 40, null = True, blank = True)
	Home_Address = models.CharField(("Home Address"), max_length = 200, null = True, blank = True)
	Email = models.EmailField(("Email"), max_length = 200, null = True, blank = True)
	Appointment_ID = models.CharField(("Appointment ID"), max_length = 55, null = True, blank = True)

	class Meta:

		verbose_name = 'DOCTOR'
		verbose_name_plural = 'DOCTORS'

	def __unicode__(self):
		return self.Doctor_ID
	
	