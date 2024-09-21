# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    task_count = tasks.count()
    debug_info = f"Number of tasks: {task_count}"
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'debug_info': debug_info})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')
        else:
            messages.error(request, 'Error adding task. Please check the form.')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def delete_task(request, task_id):  # Accept `task_id` from the URL
    task = get_object_or_404(Task, id=task_id)  # Use `task_id` from the URL
    task.delete()
    messages.success(request, f'Task "{task.name}" deleted successfully!')
    return redirect('task_list')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    messages.success(request, f'Task "{task.name}" marked as complete!')
    return redirect('task_list')
