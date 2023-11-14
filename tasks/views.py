from django.shortcuts import render, HttpResponse
from .models import Tasks, Category


def home(request):
    return render(request, "home.html")


@login_required
def tasks_read(request):
    tasks = Tasks.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user)

    context = {"tasks": [tasks], "categories": [categories]}

    return render(request, "tasks_read.html", context)
