# lux/urls.py
from django.urls import path
from lux import views
urlpatterns = [
    path("", views.home, name='home'),
]