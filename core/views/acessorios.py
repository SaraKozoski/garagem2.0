from rest_framework.viewsets import ModelViewSet
#So copia e cola o que ta aqui

from core.models import Acessorios
from core.serializers import AcessoriosSerializer


class AcessoriosViewSet(ModelViewSet):
    queryset = Acessorios.objects.all()
    serializer_class = AcessoriosSerializer
#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
