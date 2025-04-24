from rest_framework.serializers import ModelSerializer
#Esse é de boa so copiar e colar
from core.models import Modelo


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"

#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
