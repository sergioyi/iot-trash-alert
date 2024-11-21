from django.shortcuts import render
from .models import Mensagem

def mensagens_view(request):
    mensagens = Mensagem.objects.all().order_by('-created_at')
    return render(request, 'mqtt_listener/mensagens.html', {'mensagens': mensagens})
