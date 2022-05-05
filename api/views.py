from functools import partial
import stat
from urllib import response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
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
		empresa = Empresas.objects.filter(**request.query_params.dict())
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

@api_view(['DELETE'])
def delete_empresas(request, pk): 
	try: 
		empresa = Empresas.objects.get(pk=pk)
	except Empresas.DoesNotExist: 
		return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
	empresa.delete()
	return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)	

@api_view(['PATCH'])
def update_empresas(request, pk):
	empresa = Empresas.objects.get(pk=pk)
	serializer = EmpresasSerializer(instance=empresa, data=request.data, partial=True, context={'pk': pk})
	if serializer.is_valid():
		serializer.update(instance=empresa, validated_data=request.data)
		return JsonResponse({'message': 'Actualizado'}, status=status.HTTP_204_NO_CONTENT)


#APIS PARA OBLIGACIONES   
@api_view(['GET'])
def view_obligaciones(request):

	# checking for the parameters from the URL
	if request.query_params:
		obligacion = Obligaciones.objects.filter(**request.query_params.dict())
	else:
		obligacion = Obligaciones.objects.all()

	# if there is something in items else raise error
	if obligacion:
		data = ObligacionesSerializer(obligacion, many=True)
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


@api_view(['DELETE'])
def delete_obligaciones(request, pk): 
	try: 
		obligacion = Obligaciones.objects.get(pk=pk)
	except Obligaciones.DoesNotExist: 
		return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
	obligacion.delete()
	return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_obligaciones(request, pk):
	obligacion = Obligaciones.objects.get(pk=pk)
	serializer = ObligacionesSerializer(instance=obligacion, data=request.data, partial=True, context={'pk': pk})
	if serializer.is_valid():
		serializer.update(instance=obligacion, validated_data=request.data)
		return JsonResponse({'message': 'Actualizado'}, status=status.HTTP_204_NO_CONTENT)


#APIS PARA PAGOS   
@api_view(['GET'])
def view_pagos(request):

	# checking for the parameters from the URL
	if request.query_params:
		pagos = Pagos.objects.filter(**request.query_params.dict())
	else:
		pagos = Pagos.objects.all()

	# if there is something in items else raise error
	if pagos:
		data = PagosSerializer(pagos, many=True)
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


@api_view(['DELETE'])
def delete_pagos(request, pk): 
	try: 
		pago = Pagos.objects.get(pk=pk)
	except Pagos.DoesNotExist: 
		return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
 
	pago.delete()
	return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_pagos(request, pk):
	pago = Pagos.objects.get(pk=pk)
	serializer = PagosSerializer(instance=pago, data=request.data, partial=True, context={'pk': pk})
	if serializer.is_valid():
		serializer.update(instance=pago, validated_data=request.data)
		return JsonResponse({'message': 'Actualizado'}, status=status.HTTP_204_NO_CONTENT)
