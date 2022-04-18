from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Empresas, Pagos, Obligaciones
from .serializers import EmpresasSerializer, ObligacionesSerializer, PagosSerializer
from rest_framework import status
# Create your views here.

#APIS PARA EMPRESAS  
@api_view(['GET'])
def view_empresas(request):

	# checking for the parameters from the URL
	if request.query_params:
		empresa = Empresas.objects.filter(**request.query_param.dict())
	else:
		empresa = Empresas.objects.all()

	# if there is something in items else raise error
	if empresa:
		data = EmpresasSerializer(empresa, many=True)
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_view_empresas(request):

    empresa = EmpresasSerializer(data=request.data)
    # validating for already existing data
    if empresa.is_valid():
        empresa.save()
        return Response(empresa.data)
    return Response(empresa.errors,status=status.HTTP_404_NOT_FOUND)

#APIS PARA OBLIGACIONES   
@api_view(['GET'])
def view_obligaciones(request):

	# checking for the parameters from the URL
	if request.query_params:
		obligacion = Obligaciones.objects.filter(**request.query_param.dict())
	else:
		obligacion = Obligaciones.objects.all()

	# if there is something in items else raise error
	if obligacion:
		data = EmpresasSerializer(obligacion, many=True)
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_view_obligaciones(request):

    obligacion = ObligacionesSerializer(data=request.data)
    # validating for already existing data
    if obligacion.is_valid():
        obligacion.save()
        return Response(obligacion.data)
    return Response(obligacion.errors,status=status.HTTP_404_NOT_FOUND)

#APIS PARA PAGOS   
@api_view(['GET'])
def view_pagos(request):

	# checking for the parameters from the URL
	if request.query_params:
		pagos = Pagos.objects.filter(**request.query_param.dict())
	else:
		pagos = Pagos.objects.all()

	# if there is something in items else raise error
	if pagos:
		data = EmpresasSerializer(pagos, many=True)
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def create_view_pagos(request):

    pagos = PagosSerializer(data=request.data)
    # validating for already existing data
    if pagos.is_valid():
        pagos.save()
        return Response(pagos.data)
    return Response(pagos.errors,status=status.HTTP_404_NOT_FOUND)