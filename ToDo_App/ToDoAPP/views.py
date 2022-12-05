from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Using the generic class based view
class TaskListView(ListView):
    model = Task
    template_name = 'list.html'
    context_object_name = 'task_key'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task_id'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update_view.html'
    context_object_name = 'task_id'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('ToDoAPP:classdetailview', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('ToDoAPP:classhome')


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
    return render(request, 'home.html', {'task_key': task})


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




