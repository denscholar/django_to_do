from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo


def home(request):
    tasks = Todo.objects.filter(is_completed=False)
    completed_tasks = Todo.objects.filter(is_completed=True)

    context = {"tasks": tasks, "completed_tasks": completed_tasks}
    return render(request, "home/index.html", context)


def add_task(request):
    task = request.POST.get("task")
    if request.method == "POST":
        Todo.objects.create(task=task)
        return redirect("home")
    return render(request, "home/index.html")


def mark_as_complete(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("home")


def mark_as_undone(request, pk):
    task = get_object_or_404(Todo, pk=pk)
    task.is_completed = False
    task.save()

    return redirect("home")


def edit_task(request, pk):
    get_task = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        new_task = request.POST.get('task', '')
        get_task.task = new_task
        get_task.save()
        return redirect('home') 

    context = {
        "get_task": get_task,
    }
    return render(request, "home/edit.html", context)


def delete_task(request, pk):
    delete_task = get_object_or_404(Todo, pk=pk)
    delete_task.delete()
    return redirect('home')
