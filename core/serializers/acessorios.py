from rest_framework.serializers import ModelSerializer
#Esse é de boa so copiar e colar
from core.models import Acessorios


class AcessoriosSerializer(ModelSerializer):
    class Meta:
        model = Acessorios
        fields = "__all__"

#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
