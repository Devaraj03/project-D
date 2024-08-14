from django.shortcuts import render,redirect
from .models import *
#from django.contrib.auth.forms  import UserChangeForm
#from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .forms import *
from django.urls import *
from django.contrib.auth import authenticate,login,logout

 
def Home(request):
    context={
        "error":""
    }
    if request.method == "POST":

        print(request.POST)

        user = authenticate(username=request.POST['username'],password=request.POST['password'])

        print(user)

        if user is not None:
            login(request,user)
            return redirect('students/')
        else:
            context={
                "error":"*Invalid username and password"
            }
            return render(request,'home.html',context)

    return render(request,'home.html',context)

def table(request):
    context={
    'all_check' : Model.objects.all()
    }
    return render(request,'table.html',context)

def students(request):
    context={
    'all_check' : Model.objects.all()
    }
    return render(request,'stddetails.html',context)

def add(request):
    context={
        'form':Modelform()
    }
    if request.method == "POST":
        form = Modelform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'add.html',context)

def deldetails(request,id):
    selected_detail=Model.objects.get(id=id)

    selected_detail.delete()

    return redirect('/students/')

def updetails(request,id):
    select_detail=Model.objects.get(id=id)
    context = {
           'form' : Modelform(instance=select_detail)
    }
    if request.method == "POST":
        form = Modelform(request.POST,instance=select_detail)
        if form.is_valid():
            form.save()
        return redirect('/students/')
    
    return render(request,'add.html',context)

def sort(request,id):
        select_detail=Model.objects.get(id=id)
        context = {
           'form' : sort(instance=select_detail)
            }
        if request.method == "POST":
          form = sort(request.POST,instance=select_detail)
          if form.is_valid():
              form.save()
          return redirect('/students/table/')

def logoutuser(request):
    logout(request)
    return redirect('/')