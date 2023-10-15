from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('warenkorb/', views.warenkorb, name="warenkorb"),
    path('kasse/', views.kasse, name="kasse"),
]
