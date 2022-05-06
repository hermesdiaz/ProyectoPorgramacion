from django.db import models


class Empresas(models.Model):
	nombre_empresa = models.CharField(max_length=255, unique=True)
	nit_empresa = models.CharField(max_length=255, unique=True)

	def __str__(self) -> str:
		return self.name


class Obligaciones(models.Model):
	id_empresa = models.ForeignKey(
	    Empresas, on_delete=models.CASCADE, null=True)
	nombre_obligacion= models.CharField(max_length=255, unique=False)
	periodicidad = models.CharField(max_length=255, unique=False)
    
	def __str__(self) -> str:
		return self.name


class Pagos(models.Model):
	id_obligacion = models.ForeignKey(
	    Obligaciones, on_delete=models.CASCADE, null=True)
	fecha_pago = models.DateField()
	valor = models.CharField(max_length=255 )

	def __str__(self) -> str:
		return self.name
