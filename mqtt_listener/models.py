from django.db import models

class Mensagem(models.Model):
    mensagem = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem: {self.mensagem}, Recebida em: {self.created_at}"
