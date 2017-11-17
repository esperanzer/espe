# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from  .models import Treatment


# Create your views here.
class HomeView(ListView):

	model = Treatment
	template_name = "treatment.html"