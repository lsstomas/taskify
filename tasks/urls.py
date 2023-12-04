from django.urls import path
from tasks import views


urlpatterns = [
    path(
        "<int:task_id>/reminder/change", views.change_reminder, name="change_reminder"
    ),
    path("<int:task_id>/delete/", views.delete_task, name="delete_task"),
    path("<int:task_id>/conclude/", views.conclude_task, name="conclude_task"),
    path("<int:task_id>/edit/", views.edit_task, name="edit_task"),
    path("add/", views.add_task, name="add_task"),
    path("list/", views.list_tasks, name="list_tasks"),
    path("", views.info, name="info"),
]
