from django.db import models


class Empresas(models.Model):
	# id_empresa = models.CharField(primary_key=True, max_length=255)
	nombre_empresa = models.CharField(max_length=255, unique=True)
	nit_empresa = models.CharField(max_length=255, unique=True)

	def __str__(self) -> str:
		return self.name


class Obligaciones(models.Model):
	id_empresa = models.ForeignKey(
	    Empresas, on_delete=models.SET_NULL, null=True)
	#nombre_empresa = models.CharField(max_length=255, unique=True)
	nombre_obligacion= models.CharField(max_length=255)
	#nit_empresa = models.CharField(max_length=255, unique=True)
	fecha_pago_obligacion = models.DateField()
	valor = models.CharField(max_length=255, unique=True)
	periodicidad = models.CharField(max_length=255, unique=True)
    
	def __str__(self) -> str:
		return self.name


class Pagos(models.Model):
	id_obligacion = models.ForeignKey(
	    Obligaciones, on_delete=models.SET_NULL, null=True)
	fecha_pago = models.DateField()

	def __str__(self) -> str:
		return self.name
