# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Signout(models.Model):

	User_Name = models.CharField(("User_Name"), max_length = 55, null = True, blank = True)
	Password = models.CharField(("Password"), max_length = 40, null = True, blank = True)

	class Meta:
		verbose_name = 'SIGNOUT'
		verbose_name_plural = 'SIGNOUTS'

	def __unicode__(self):

		return self.Patient_ID
