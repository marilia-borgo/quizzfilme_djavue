from django.urls import path

from . import views

urlpatterns = [
    path("add", views.recebe_resultado),
    path("", views.get_resultado),
]
