from django.urls import path
from blog.views import *
from blog.models import  *


urlpatterns = [
    path('',Home,name='home'),
    path('students/table/',table,name='table'),
    path('students/',students,name='students'),
    path('students/add/',add,name='add'),
    path('logout/',logoutuser,name='logout'),
    path('students/delete/<int:id>/',deldetails,name='stddelete'),
    path('students/update/<int:id>/',updetails,name='updatestd'),
]
