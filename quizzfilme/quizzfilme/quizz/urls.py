from django.urls import path

from . import views

urlpatterns = [
    path("add", views.recebe_resultado),
    path("", views.get_resultado),
    path('rate/<int:post_id>/<int:rating>/', views.rate),
    path('resultado/', views.save_note),
]
