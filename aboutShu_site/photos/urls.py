from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("index/", views.index, name = "index"),
    path("flower/", views.flower, name = "flower"),
    path("landscape/", views.landscape, name = "landscape"),
    path("city/", views.city, name = "city"),
    path("lighting/", views.lighting, name = "lighting"),
]