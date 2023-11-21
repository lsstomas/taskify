from django.shortcuts import render, HttpResponse
from .models import Task, Category


def home(request):
    return render(request, "tasks/home.html")


def tasks_list(request):
    tasks = Task.objects.all()

    return render(request, "tasks/tasks_list.html", {"tasks": tasks})


def contact(request):
    return render(request, "tasks/contact.html")
