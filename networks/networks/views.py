from django.shortcuts import HttpResponse, render 

def login(request):
	""" Function doc """
	return render(request, "auth-login.html")

def info(request):
	'''Funcion principal'''
	return render(request,"base.html")