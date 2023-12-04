from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, "website/home.html")


def contact(request):
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
