from cmath import log
import re
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from servers.models import ServerDetails
from .forms import ServerDetailsForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        userform = CreateUserForm()

        if request.method == 'POST':
            userform = CreateUserForm(request.POST)
            if userform.is_valid():
                userform.save()
                user = userform.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user )

                return redirect('login')

        context = {'form':userform}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('addandshow')
            else:
                messages.info(request,'username or password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def addserver(request):
    if request.method == 'POST':
        fm = ServerDetailsForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = ServerDetailsForm()
    else:
        fm = ServerDetailsForm()
    return render(request, 'addserver.html', {'form':fm })

@login_required(login_url='login')
def showserver(request):
    show_servers = ServerDetails.objects.all()
    return render(request, 'showserver.html', {'show': show_servers})

#adding new items and show all items
@login_required(login_url='login')
def add_show(request):
    if request.method == 'POST':
        fm = ServerDetailsForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = ServerDetailsForm()
    else:
        fm = ServerDetailsForm()
    show_servers = ServerDetails.objects.all()
    return render(request, 'addandshow.html', {'form':fm , 'show': show_servers})

#delete funcction
@login_required(login_url='login')
def delete_data(request,id):
    if request.method == 'POST':
        values = ServerDetails.objects.get(pk=id)
        values.delete()
        return HttpResponseRedirect('/')

#update function
@login_required(login_url='login')
def update_data(request, id):
    if request.method == 'POST':
        serverdetail = ServerDetails.objects.get(pk=id)
        form=ServerDetailsForm(request.POST, instance=serverdetail)
        if form.is_valid():
            form.save()
    else: 
        serverdetail = ServerDetails.objects.get(pk=id)
        form=ServerDetailsForm(instance=serverdetail)
    return render(request, 'updateserver.html', {'form':form} )

