from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.
def task(request):
    task = Task.objects.all()
    if request.method == 'POST':
        task1 = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task_s = Task(task=task1, priority=priority, date=date)
        task_s.save()
        return redirect('/')
    return render(request, 'home.html',{'task_key': task})


def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})




