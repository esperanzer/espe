# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse 

# class HomeView(HomeView):
# 	model = home 
# 	template_name = 'base/base.html'

def index(request):
	return render(request, 'index.html')

# Create your views here.
