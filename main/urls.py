from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("owner_reusable_items",
         views.owner_reusable_items,
         name="owner_reusable_items"),
    path("register_owner",
         views.register_owner,
         name="register_owner"),
    path("register_reusable_item",
         views.register_reusable_item,
         name="register_reusable_item"),
    path("reusable_items",
         views.reusable_items,
         name="reusable_items"),
]
