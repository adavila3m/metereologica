from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import HttpResponse, render 
from autogestion.models import sitio, medicion

def login(request):
	""" Function doc """
	return render(request, "auth-login.html")

def info(request):
	'''Funcion principal'''
	return render(request,"base.html")

def dashboard(request, template_name= None):
	#consultar sitios
	sitios = sitio.objects.all()
	titulo = "NODOS"
	
	return render(	request,
					"dashboard.html",
					{	"sitios":sitios,
	  					"titulo": titulo,  				

					},
							
	)

def mediciones(request,id):
	#consultar sitios
	a = sitio.objects.get(id=id)
	
	mediciones = a.mediciones.all().order_by('-fecha')
	
	return render(	request,
					"mediciones.html",
					{	"mediciones":mediciones,
	  					"titulo": "LECTURA DE VARIABLES AMBIENTALES",
						"nodo": a.nombre,
						  	  
					},
							
	)

@api_view(['POST'])
def recibir_datos(request):
	dato = request.data
	inst = sitio.objects.get(nombre="IFTS 24")

	if dato:
		# Guardar el dato en la base de datos
		med = medicion.objects.create(**dato)
		inst.mediciones.add(med)
		inst.save()
		
		return Response({"message": "Dato recibido correctamente"}, status=status.HTTP_201_CREATED)
	return Response({"error": "Dato no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)