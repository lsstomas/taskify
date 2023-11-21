from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.tasks_list, name="tasks_list"),
    path("contact/", views.contact, name="contact"),
]
