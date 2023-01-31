from django.urls import path

from . import views 

urlpatterns = [
    path('<int:id>', views.details, name="fetch_details"),
    path('rooms', views.room_list, name="rooms"),
    path('new', views.new, name="new"),
    
]

