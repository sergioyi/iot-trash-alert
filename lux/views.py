# lux/views.py
from django.shortcuts import render
def home(request):
    return render(request, "lux/home.html", {})
# Aqui foi criado um código responsável por renderizar um arquivo html chamado “home.html”.