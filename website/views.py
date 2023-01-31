from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request, 'website/landing.html', {'name':'Ashutosh Pandey', 'profile_link':'https://www.linkedin.com/in/ashutosh-pandey10', 
    'meetings' : Meeting.objects.all()})
    # As is written above every mode class has method "objects" to perform several operations over it.
    # And this is exactly what we will leverage here.

    # objects.all() returns a list of all the objects that are present inside the db instantiated by model class "Meeting" 
    
        
def date(request):
    '''
    This is just to show that evertime we a get request is made this function is executed.
    '''
    return HttpResponse(f"Current date and time are {str(datetime.now())}")

def about(request):
    return HttpResponse(f"I am Ashutosh and I develop nice, minimalist python backends for Infineon.")
    