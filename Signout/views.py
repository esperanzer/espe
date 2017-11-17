# -*- coding: utf-8 -*-s
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Signout

# Create your views here.

class HomeView(ListView):
	model = Signout
	template_name = "signout.html"
