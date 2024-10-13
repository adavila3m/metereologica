from django.db import models

# Create your models here.

class medicion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    temperatura = models.FloatField()
    humedad = models.FloatField()
    presion = models.FloatField()
    nivel_sonido = models.FloatField()
    

    def __str__(self):
        return f"Fecha:{self.fecha}, Temperatura: {self.temperatura}"

class sitio(models.Model):
    nombre = models.CharField(max_length=50,)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    mediciones = models.ManyToManyField(medicion)

    def __str__(self):
        return f"Nombre: {self.nombre}, Direccion: {self.direccion}"

    
class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp: {self.temperature}, Humidity: {self.humidity}, Time: {self.timestamp}"
