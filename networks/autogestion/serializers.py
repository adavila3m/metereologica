# serializers.py

from rest_framework import serializers
from .models import SensorData, medicion

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity', 'timestamp']

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicion
        fields = ['fecha','temperatura','humedad','presion','nivel_sonido']