from django.urls import path
from . import views

urlpatterns = [
    path('<str:songName>', views.getSong, name="getSong")
]