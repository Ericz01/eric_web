from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Eric", views.Eric, name="Eric"),
    path("<str:name>", views.greet, name="name")
]