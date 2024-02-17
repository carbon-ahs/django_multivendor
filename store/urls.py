from django.urls import path

from . import views


# from .views import say_hello

urlpatterns = [
    path("<slug:slug>/", views.product_detail, name="product_detail"),
]
