from django.shortcuts import render
from django.forms import modelform_factory   
from meetings.models import Meeting, Room

# Create your views here.
def details(request, id): # The second argument will be passed through the URL itself
    meeting = Meeting.objects.get(pk = id)

    return render(request, 'meetings/details.html', {'meeting':meeting})


# Details of all the rooms
def room_list(request):
    rooms = Room.objects.all()

    return render(request, 'meetings/rooms.html', {'rooms':rooms})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    form = MeetingForm()
    return render(request, 'meetings/new.html', {'form':form})