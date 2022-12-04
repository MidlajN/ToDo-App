from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Task


# Create your views here.
def task(request):
    task = Task.objects.all()
    if request.method == 'POST':
        task1 = request.POST.get('task')
        priority = request.POST.get('priority')
        task_s = Task(task1=task1, priority=priority)
        task_s.save()
        return redirect('/')
    return render(request, 'home.html',{'task_key': task})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

