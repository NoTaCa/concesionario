from django.db import models

class Auto(models.Model):
    placa = models.CharField(max_length=17, unique=True)  # VIN#
    marca = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    foto = models.ImageField(upload_to='autos')
    kilometraje = models.PositiveIntegerField()
    modelo = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)  # TRIM del auto
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.placa
