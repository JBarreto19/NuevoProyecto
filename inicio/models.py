from django.db import models

class Concierto (models.Model):
    banda = models.CharField(max_length=30)
    genero = models.TextField()
    precioEntrada = models.IntegerField()

    def __str__(self):
        return f'{self.id} - {self.banda} - {self.genero} -{self.precioEntrada}'

