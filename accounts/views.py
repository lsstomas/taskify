from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def register_view(request):
    if request.method == "GET":
        return render(request, "accounts/register.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe!")
            return render(request, "accounts/register.html")

        if password1 != password2:
            messages.error(request, "As senhas devem ser iguais!")
            return render(request, "accounts/register.html")

        user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        user.save()

        messages.success(request, "Usuário criado com sucesso!")
        return redirect("login")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logado com sucesso!")
            return redirect("info")
        else:   
            messages.error(request, "Usuário ou senha inválidos!")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return redirect("login")
