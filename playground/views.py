from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Not to be misunderstood by frontend views
# It the part of an app where it handles http requests and responses

def say_hello(request):
    return HttpResponse("Hello World!")