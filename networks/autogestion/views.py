from django.shortcuts import render

# Create your views here.
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData, sitio
from .serializers import SensorDataSerializer, MedicionSerializer

class SensorDataView(APIView):
    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicionDataView(APIView):
    def post(self, request):
        serializer = MedicionSerializer(data=request.data)
        if serializer.is_valid():
            #med = serializer.save()
            sitio = sitio.objects.get(id=1)
            sitio.mediciones.add(serializer.save())
            sitio.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
