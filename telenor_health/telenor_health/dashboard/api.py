from models import FactTable
from serializers import FactSerializer
from rest_framework import generics


class FactList(generics.ListCreateAPIView):
    queryset = FactTable.objects.all()
    serializer_class = FactSerializer
