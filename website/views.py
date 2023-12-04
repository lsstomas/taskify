from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from website.forms import ContactForm

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def home(request):
    return render(request, "website/home.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]

            try:
                send_mail(
                    subject + " - " + name + " - " + sender,
                    message,
                    settings.EMAIL_HOST_USER,
                    ["luisftomasprado@gmail.com"],
                    fail_silently=False,
                )
            except Exception:
                messages.error(request, "ERRO: Ocorreu um erro ao enviar a mensagem.")
                return redirect("contact")

            messages.success(request, "Mensagem enviada com sucesso!")
            return redirect("contact")
        else:
            messages.error(request, "ERRO: Ocorreu um erro ao enviar a mensagem.")
            return redirect("contact")

    return render(request, "website/contact.html")


@login_required(login_url="/accounts/login/")
def settings(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        user = request.user

        if (
            (user.first_name == first_name)
            and (user.last_name == last_name)
            and (user.email == email)
        ):
            context = {
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "email": request.user.email,
            }
            messages.info(request, "Nenhuma alteração foi feita.")
            return render(request, "website/settings.html", context)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request, "Configurações salvas com sucesso.")

    context = {
        "first_name": request.user.first_name,
        "last_name": request.user.last_name,
        "email": request.user.email,
    }

    return render(request, "website/settings.html", context)
