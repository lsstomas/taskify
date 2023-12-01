from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from categories.models import Category
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


@login_required(login_url="/accounts/login/")
def info(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    pendent_tasks = tasks.filter(status="N").count() + tasks.filter(status="P").count()
    tasks_completed = tasks.filter(status="C").count()

    context = {
        "total_tasks": total_tasks,
        "pendent_tasks": pendent_tasks,
        "tasks_completed": tasks_completed,
    }

    return render(request, "tasks/info.html", context)


@login_required(login_url="/accounts/login/")
def list_tasks(request):
    tasks = Task.objects.filter(user=request.user)

    return render(request, "tasks/list_tasks.html", {"tasks": tasks})


@login_required(login_url="/accounts/login/")
def add_task(request):
    categories = Category.objects.filter(user=request.user)
    form = TaskForm(user=request.user)

    if request.method == "POST":
        form = TaskForm(user=request.user, data=request.POST)

        if form.is_valid():
            task = form.save(commit=False)

            task.user = request.user
            category_name = request.POST.get("task_category")
            if category_name:
                category = get_object_or_404(
                    Category, name=category_name, user=request.user
                )
                task.category = category

            task.save()
            messages.success(request, "SUCESSO: Tarefa adicionada com êxito.")
            return redirect("list_tasks")
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao adicionar a tarefa.")

    return render(
        request, "tasks/add_task.html", {"form": form, "categories": categories}
    )


@login_required(login_url="/accounts/login/")
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    form = TaskForm(instance=task, user=request.user)
    categories = Category.objects.filter(user=request.user)

    if request.method == "POST":
        form = TaskForm(data=request.POST, instance=task, user=request.user)

        if form.is_valid():
            task = form.save(commit=False)

            category_name = request.POST.get("task_category")
            if category_name:
                category = get_object_or_404(
                    Category, name=category_name, user=request.user
                )
                task.category = category

            task.save()
            messages.success(request, "SUCESSO: A tarefa foi editada com êxito.")
            return redirect("list_tasks")
        else:
            print(form.errors)
            messages.error(request, "ERRO: Ocorreu um erro ao editar a tarefa.")

    return render(
        request,
        "tasks/edit_task.html",
        {
            "form": form,
            "task": task,
            "categories": categories,
        },
    )


@login_required(login_url="/accounts/login/")
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "GET":
        task.delete()
        messages.success(request, "SUCESSO: A tarefa foi excluída com êxito.")
    else:
        messages.error(request, "ERRO: Ocorreu um erro ao excluir a tarefa.")

    return redirect("list_tasks")


@login_required(login_url="/accounts/login/")
def conclude_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        if task.status == "C":
            messages.error(request, "ERRO: A tarefa já está concluída.")
            return redirect("list_tasks")

        task.status = "C"
        task.conclution_date = timezone.localtime(timezone.now())
        task.save()
        messages.success(request, "SUCESSO: A tarefa foi concluída com êxito.")
    else:
        messages.error(request, "ERRO: Ocorreu um erro ao concluir a tarefa.")

    return redirect("list_tasks")
