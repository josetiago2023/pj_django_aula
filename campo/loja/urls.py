from django.comtrib import admin
from django.urls import path

urlpatters = [
    path("pesquisar", views.pequisar, name="pesquisar")
]