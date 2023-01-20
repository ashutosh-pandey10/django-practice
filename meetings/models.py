from datetime import time
from django.db import models

# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    floor_no = models.IntegerField()
    room_no = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.room_name}-{self.room_no} Floor {self.floor_no}."

class Meeting(models.Model):
    title = models.TextField(max_length=200)
    date = models.DateField()

    # Adding two more fields in DB
    start_time = models.TimeField(default=time(9)) 
    # Here default values are added as I have already created 2 records in the db
    # Now to add the colunmns to the table I'll have to add values to the records created earlier else
    # the empty columns will not be added. 
    duration = models.IntegerField(default=30)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # This is a property of foriegn key relation while working with django,
    # one has to specify what will happen if the room record from the primary table is 
    # deleted. It will remove all the records from the meeting table corresponding
    # to that particular "room" record.

    # This is to return the string, whenever object of the class is instantiated and print() method is called over it.
    def __str__(self) -> str:
        return f"{self.title} on {self.date} from {self.start_time} onwards for {self.duration} minutes."

