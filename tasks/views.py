from django.shortcuts import render, HttpResponse
from .models import Task, Category
from django.contrib.auth import login, authenticate


def home(request):
    return render(request, "tasks/home.html")


def tasks_list(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }

    return render(
        request, 
        "tasks/tasks_list.html", 
        context)


def contact(request):
    return render(request, "tasks/contact.html")
