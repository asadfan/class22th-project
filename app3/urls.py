from django.urls import path
from app3.views import *
app_name='asadapp'
urlpatterns=[
    path('asad/',asad,name='asad')
]