from rest_framework.viewsets import ModelViewSet
#So copia e cola o que ta aqui

from core.models import Modelo
from core.serializers import ModeloSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
