# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Appointment(models.Model):

	Appointment_ID= models.CharField(("Appointment_ID"), max_length = 55, null = True, blank = True)
	Patient_ID = models.CharField(("Patient ID"), max_length = 55, null = True, blank = True )
	Patient_Name = models.CharField(("Patient Name"), max_length = 40, null = True, blank = True)
	Gender = models.CharField(("Gender(F or M )"), max_length = 1)
	Home_Address = models.CharField(("Home Address"), max_length = 100, null = True, blank = True)
	Date_Of_Appointment = models.DateTimeField(("Date of Appointment"))
	Email = models.EmailField(("Email"), max_length = 255, null = True, blank = True)
	Treatment_ID = models.CharField(("Treatment ID"), max_length = 55, null = True, blank = True)

	class Meta:

		verbose_name ='APPOINTMENT'
		verbose_name_plural = 'APPOINTMENTS'

	def __unicode__(self):
		return self.Appointment_ID

