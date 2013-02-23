from django.http import HttpResponse
from django.shortcuts import render
from neighbors.models import User, Request

def homepage(request):
	return render(request, 'homepage.html')

def messagepage(request):
	return render(request, 'messagepage.html')