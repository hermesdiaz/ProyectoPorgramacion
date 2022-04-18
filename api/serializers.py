from rest_framework import serializers
from .models import Empresas,Pagos,Obligaciones

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = "__all__"

class PagosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = "__all__"

class ObligacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obligaciones
        fields = "__all__"
