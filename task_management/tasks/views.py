from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_detail(request, pk):
  task = get_object_or_404(Task, pk=pk)
  return render(request, 'task_detail.html', {'task': task})

def create_task(request):
  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      task = form.save()
      return redirect('task_detail', pk=task.pk)
  else:
    form = TaskForm()
  return render(request, 'create_task.html', {'form': form})