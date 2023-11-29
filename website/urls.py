from django.urls import path
from website import views

urlpatterns = [
    path("settings/", views.settings, name="settings"),
    path("contact/", views.contact, name="contact"),
    path("", views.home, name="home"),
]
