from django.conf import settings
from django.db import models
from django.utils import timezone


class Escorpiao(models.Model):
    presenca = models.CharField(max_length=200)
    data_encontro = models.DateTimeField(default=timezone.now)
    

    def publish(self):
        self.data_encontro = timezone.now()
        self.save()

    # def __str__(self):
    #     return self.title