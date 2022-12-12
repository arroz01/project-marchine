from django.db import models
from django.utils import timezone


# Create your models here.
class Marchine(models.Model):
    valor = models.IntegerField(default=0)
    acao = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.valor}'

    class Meta:
        verbose_name = 'Marchine'
        verbose_name_plural = 'Marchines'
        ordering = ['-data_criacao']
