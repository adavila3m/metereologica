from django.contrib import admin
from autogestion.models import SensorData, sitio, medicion

# Register your models here.
admin.site.register(SensorData)
admin.site.register(sitio)
admin.site.register(medicion)