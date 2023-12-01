from django.shortcuts import render, redirect, get_object_or_404
from categories.models import Category
from .forms import CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


@login_required(login_url="/accounts/login/")
def list_categories(request):
    categories = Category.objects.filter(user=request.user)

    return render(
        request, "categories/list_categories.html", {"categories": categories}
    )


@login_required(login_url="/accounts/login/")
def add_category(request):
    form = CategoryForm(user=request.user)

    if request.method == "POST":
        form = CategoryForm(user=request.user, data=request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, "SUCESSO: Categoria adicionada com êxito.")
            return redirect("list_categories")
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao adicionar a categoria.")

    return render(
        request,
        "categories/add_category.html",
        {"form": form, "user": request.user},
    )


@login_required(login_url="/accounts/login/")
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)
    form = CategoryForm(instance=category, user=request.user)

    if request.method == "POST":
        form = CategoryForm(data=request.POST, instance=category, user=request.user)

        if form.is_valid():
            category = form.save(commit=False)
            
            category.user = request.user
            category.save()
            messages.success(request, "SUCESSO: A categoria foi editada com êxito.")
            return redirect("list_categories")
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao editar a categoria.")

    return render(
        request,
        "categories/edit_category.html",
        {"form": form, "category": category, "user": request.user},
    )


@login_required(login_url="/accounts/login/")
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)

    if request.method == "GET":
        category.delete()
        messages.success(request, "SUCESSO: A categoria foi excluída com êxito.")
    else:
        messages.error(request, "ERRO: Ocorreu um erro ao excluir a categoria.")

    return redirect("list_categories")
