# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):

	Login = models.CharField(("Login"), max_length = 55, null = True, blank = True)
	Password = models.CharField(("Password"), max_length = 40, null = True, blank = True)
	
	class Meta:
		verbose_name = 'LOGIN'
		verbose_name_plural = 'LOGINS'

	def __unicode__(self):
		
		return self.User_Name
