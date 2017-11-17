# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):

	User_ID = models.CharField(("User ID"), max_length = 55, null = True, blank = True ) 
	User_Name = models.CharField(("User Name"), max_length = 55, null = True, blank = True)
	Password = models.CharField(("Password "), max_length = 55)
	Gender = models.CharField(("Gender(M or F)"), max_length = 1)
	Home_Address = models.CharField(("Home Dddress"), max_length = 255, null=True, blank = True)
	Email = models.EmailField(("Email"), max_length = 100, null = True, blank = True) 
	Contact_Number = models.CharField(("Contact Number"), max_length = 20, null = True, blank = True)

	class Meta:

		verbose_name = 'USER'
		verbose_name_plural = 'USERS'

		def __unicode__(self):
			return self.User_ID
