from django.shortcuts import render, redirect
from todoapp.models import Contact
from todoapp.models import Task
from todoapp.models import Owner
from todoapp.models import Finalowner
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

# Create your views here.



def home(request):
   return render(request, 'home.html')



def about(request):
        
    return render(request, 'about.html')



def contact(request):
    
    context = {'success': False }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name = name, email= email, phone = phone, desc = desc)
        ins.save()
        context = {'success': True }

    return render(request, 'contact.html', context)


def welcome(request):
    return render(welcome.html)

def loginuser(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        global glo
        username = request.POST['username']
        glo = username
        password = request.POST['password']
        user = authenticate(username= username, password = password)

        if user is not None:
            login(request, user)
            # return redirect("/todo")      
            context = {'name':username}
            return render(request, 'welcome.html',context)
            context = {'successs':False}


        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)
    


def register(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if ( len(username) or len(first_name) or len(last_name) or len(email) or len(password1)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (User.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            

        elif ( User.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            ins = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
            ins.save()
            context = {'success': True}

    return render(request, 'register.html', context)






def owner(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        images = request.POST['images']

        if ( len(username) or len(first_name) or len(last_name) or len(email)  )== 0:
            context={'successs':True,'mssg':"Please enter every field!!"}


        elif (Owner.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            

        elif ( Owner.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            ins = Owner(username = username, first_name = first_name, last_name = last_name, email = email, images = images)
            ins.save()
            context = {'success': True}
            return render(request, 'owner.html', context)


    return render(request, 'owner.html', context)


def add(request):
    so = Owner.objects.all()
    context = {'so': so}
    return render(request, 'admin.html', context)


def delete(request, name):
    abc = Owner.objects.get(username = name)
    abc.delete()
    return redirect("/add")


def view(request, obj, obj2, obj3, obj4, obj5):
    context = {'name': obj, 'first_name': obj2, 'last_name': obj3, 'email': obj4, 'phone': obj5}
    return render(request, 'view.html', context)


def accept(request, obj, obj2, obj3, obj4, obj5):
    xyz = Finalowner(username = obj, first_name = obj2, last_name = obj3, email = obj4, phone = obj5)
    xyz.save()
    abc = Owner.objects.get(username = obj)
    abc.delete()
    return redirect("/add")
    
