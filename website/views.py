from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the landing page!")

def date(request):
    '''
    This is just to show that evertime we a get request is made this function is executed.
    '''
    return HttpResponse(f"Current date and time are {str(datetime.now())}")

def about(request):
    return HttpResponse(f"I am Ashutosh and I develop nice, minimalist python backends for Infineon.")
    