# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
class HomeView(ListView):
	model = User
	template_name = "user.html"
