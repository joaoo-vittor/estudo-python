from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerialiser


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerialiser
