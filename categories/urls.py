from django.urls import path
from categories import views


urlpatterns = [
    path("<int:category_id>/delete/", views.delete_category, name="delete_category"),
    path("<int:category_id>/edit/", views.edit_category, name="edit_category"),
    path("add/", views.add_category, name="add_category"),
    path("", views.list_categories, name="list_categories"),
]