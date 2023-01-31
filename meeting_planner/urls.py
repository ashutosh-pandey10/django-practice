"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website.views import about, welcome, date

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('welcome', website.views.welcome),
    path("", welcome, name="index_page"), # Served this function at initial endpoint
    path("date", date),
    path("about", about),
    
    # path("meetings/<int:id>", details, name="fetch_details"), # "name" added for url mapping! Refer to landing.html in website app 
    # path("rooms", room_list, name="rooms"),

    # A good practice for mapping urls to views will be to start a url under same appplication with the same prefix
    path('meetings/', include('meetings.urls')),


]
