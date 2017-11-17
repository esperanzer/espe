# -*- coding: utf-8 -*-s
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Login

# Create your views here.

class HomeView(ListView):
	model = Login
	template_name = "login.html"
