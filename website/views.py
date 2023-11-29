from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "website/home.html")


def contact(request):
    return render(request, "website/contact.html")


@login_required(login_url="/accounts/login/")
def settings(request):
    return render(request, "website/settings.html")
