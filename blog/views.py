from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def viewDashboard(request):
	return HttpResponse("Blog Dashboard Page loaded!")

def viewProfile(request):
	return HttpResponse("Profile Page loaded!")