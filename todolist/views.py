import imp
from turtle import title
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from pytz import timezone
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from todolist.forms import CreateTask
from django.core import serializers
import datetime
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user = request.user
    data_todolist = Task.objects.filter(user__pk=user.pk)
    context = {
        'username' : user.username,
        'todolist' : data_todolist,
        
    }
    return render (request, "todolist_ajax.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    #user = request.user
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        #Task.objects.create(user_id=user.id, title=title, description=description, date=date)
            return redirect ('todolist:show_todolist')
        else:
            form = CreateTask(initial={'user': request.user})
    context = {'form':form}
    return render(request, 'createtask.html', context)


def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add(request):
    
    if request.user.is_authenticated:
        form = CreateTask(request.POST)
        response_data = {}
        if request.method == 'POST' and form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            taskNew = Task.objects.create(title=title, description=description,
                                                user=request.user, date=datetime.now() )
            response_data['title'] = title
            response_data['description'] = description
            response_data['date'] = datetime.now()
            taskNew.save()
            return JsonResponse(response_data)

        context = {
            'form': form,
        }
        return render(request, 'todolist.html', context)
        
    else:
        return redirect('todolist:login')