from rest_framework.viewsets import ModelViewSet
#So copia e cola o que ta aqui
from core.models import Veiculo
from core.serializers import VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
