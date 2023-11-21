from django.shortcuts import render, HttpResponse


def login(request):
    return HttpResponse("Login")


def signup(request):
    return HttpResponse("Signup")
