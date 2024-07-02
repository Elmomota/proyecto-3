from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import taskform
from .models import task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sigup(request):

    if request.method == 'GET':
        return render(request, 'main.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:

                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')

            except IntegrityError:
                return render(request, 'main.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })

        return render(request, 'main.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no coincide'
        })
@login_required
def tasks(request):
    tasks=task.objects.filter(user=request.user, datecompleted__isnull=True)

    return render(request, 'tasks.html',{'tasks':tasks})
@login_required
def completed_tasks(request):
    tasks=task.objects.filter(user=request.user, datecompleted__isnull=False).order_by
    ('-datecompleted')

    return render(request, 'tasks.html',{'tasks':tasks})
@login_required
def create_tasks(request):

    if request.method=='GET':

        return render(request,'create_task.html',{
            'form':taskform
        })
    else:
        try:
            form =  taskform(request.POST)
            new_task=form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request,'create_task.html',{
            'form':taskform,
            'error':'lugar proporcionar datos válidos '
        })
@login_required
def detail_tasks(request,task_id):
    if request.method=='GET':
        tasks=get_object_or_404(task,pk=task_id, user=request.user)
        form=taskform(instance=tasks)
        return render(request, 'task_detail.html',{'tasks':tasks,'form':form})
    else:

        try:
            tasks=get_object_or_404(task,pk=task_id, user=request.user)
            form=taskform(request.POST, instance=tasks)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html',{'tasks':tasks,'form':form,
                                                       'error': "Error al actualizar la tarea"})
@login_required
def complete_task(request,task_id):
    tasks=get_object_or_404(task, pk=task_id,user=request.user)
    if request.method=='POST':
        tasks.datecompleted=timezone.now()
        tasks.save()
        return redirect('tasks')
@login_required   
def delete_task(request,task_id):
    tasks=get_object_or_404(task, pk=task_id,user=request.user)
    if request.method=='POST':
        tasks.delete()
        return redirect('tasks')
@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user=authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'El nombre de usuario o la contraseña son incorrectos'
        })
        else:
            login(request, user)
            return redirect('tasks')

