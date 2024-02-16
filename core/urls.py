from django.urls import path

from core import views


# from .views import say_hello

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("about/", views.about, name="about"),
    path("test/", views.home, name="home"),
]
