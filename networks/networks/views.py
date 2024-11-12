from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import HttpResponse, render 
from autogestion.models import sitio, medicion
from django.core.paginator import Paginator

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

def mediciones2(request,id):
	#consultar sitios
	a = sitio.objects.get(id=id)
	mediciones = a.mediciones.all().order_by('-fecha')

	paginator = Paginator(mediciones, 10)  # 10 elementos por página

	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	
	return render(	request,
					"mediciones2.html",
					{	"page_obj": page_obj,
						"mediciones":mediciones,
	  					"titulo": "LECTURA DE VARIABLES AMBIENTALES (DOS)",
						"nodo": a.nombre,
						  	  
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

	try:
		if dato["nodo"]:
			inst = sitio.objects.get(nombre=dato["nodo"])
	except Exception as e:
		print(f"Ocurrio el siguiente Error: {e}")
		

	if dato:
		# Guardar el dato en la base de datos
		med = medicion.objects.create(temperatura=dato["temperatura"],humedad=dato["humedad"], presion = dato["presion"], nivel_sonido=dato["nivel_sonido"])
		inst.mediciones.add(med)
		inst.save()
		
		return Response({"message": "Dato recibido correctamente %s"%(inst.nombre,)}, status=status.HTTP_201_CREATED)
	return Response({"error": "Dato no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)