from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Fotografia(models.Model):

    opcoes = [
        ('Economicas', 'Econômicas'),
        ('Japonesa', 'Japonesa'),
        ('Doces', 'Doces'),
        ('Lanches', 'Lanches'),
        ('Italiana', 'Italiana'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes, default='')
    descricao = models.TextField(max_length=15000, null=False, blank=False)
    ingredientes = models.TextField(max_length=15000, null=False, blank=False, default='')
    modo_preparo = models.TextField(max_length=15000, null=False, blank=False, default='')
    foto = models.ImageField(upload_to='fotos/%Y%m%d/', blank=True )
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )



    def __str__(self):
        return self.nome
