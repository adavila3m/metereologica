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
	titulo = "Sitios"
	
	return render(	request,
					"dashboard.html",
					{	"sitios":sitios,
	  					"titulo": titulo,  				

					},
							
	)

def mediciones(request, template_name= None):
	#consultar sitios
	a = sitio.objects.get(id=1)
	mediciones = a.mediciones.all().order_by('-fecha')
	
	return render(	request,
					"mediciones.html",
					{	"mediciones":mediciones,
	  					"titulo": "Mediciones",	  
					},
							
	)