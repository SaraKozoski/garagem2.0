from rest_framework.serializers import ModelSerializer
#Esse é de boa so copiar e colar
from core.models import Veiculo


class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
