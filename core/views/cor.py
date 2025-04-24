from rest_framework.viewsets import ModelViewSet
#So copia e cola o que ta aqui

from core.models import Cor
from core.serializers import CorSerializer


class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
#NAO ESQUECEEEE DE COLOCAR NO _INIT_.PY
