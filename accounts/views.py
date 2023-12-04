from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def register_view(request):
    if request.method == "POST":
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

        email_body = render_to_string(
            "accounts/email_template.html", {"name": request.POST.get("username")}
        )

        send_mail(
            "Confirmação de Cadastro!",
            email_body,
            settings.EMAIL_HOST_USER,
            [email if email else "luisftomasprado@gmail.com"],
            fail_silently=False,
        )

        return redirect("login")

    return render(request, "accounts/register.html")


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


def password_reset(request):
    if request.method == "POST":
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user = request.user

        if user.check_password(password):
            if password1 == password:
                messages.error(request, "A nova senha deve ser diferente da atual!")
                return render(request, "accounts/password_reset.html")

            if password1 == password2:
                user.set_password(password1)
                user.save()
                messages.success(request, "Senha alterada com sucesso!")
                logout(request)
                return redirect("login")
            else:
                messages.error(request, "A nova senha não confere! Digite novamente...")
                return redirect("password_reset")
        else:
            messages.error(request, "Senha atual inválida!")
            return redirect("password_reset")

    return render(request, "accounts/password_reset.html")
