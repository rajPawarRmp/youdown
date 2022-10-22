from django.contrib import admin
from django.urls import path , include
from . import views
app_name = 'my_project'
urlpatterns = [
    
    path('' ,views.home),
    path('download' ,views.download),
    
    path('download/<resolution>' ,views.downloaded, name="downloaded"),
    path('download/' ,views.downloaded_audio, name="downloaded_audio"),
    path('download/done' ,views.done),
   
]
