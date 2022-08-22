from django.shortcuts import render, redirect
from .models import Task
import datetime
from.forms import AddTaskForm

# Create your views here.
def home(request):
    tasks=Task.objects.filter(is_completed=False, due_datetime__gte=datetime.datetime.now()).order_by('-due_datetime')
    now=datetime.datetime.now()
    
    context={'t':tasks,"n":now}
    return render(request,"index.html",context)

def every_task(request):
    tasks=Task.objects.all().order_by('-due_datetime')
    now=datetime.datetime.now()
    context={'t':tasks,"n":now}
    return render(request,"all.html",context)

def add_task(request):
    if request.method=="POST":
        form=AddTaskForm(request.POST)
        if form.is_valid():
            t=Task()
            t.task=form.cleaned_data['task']
            t.due_datetime=form.cleaned_data['due_datetime']
            t.is_completed=form.cleaned_data['is_completed']
            t.save()
    form=AddTaskForm()


    return render(request,"add_task.html",{"form":form})


def completed(request,pk):
    o=Task.objects.filter(pk=pk).update(is_completed=True)
    
    return redirect('home')

def delete(request, pk):
    o=Task.objects.filter(pk=pk).delete()
    
    return redirect('all')

def search(request):
        item=str(request.POST['search_bar'])
        print(item)
        o=Task.objects.filter(task=item)

        