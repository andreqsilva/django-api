from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


class CursosAPIViews(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class CursoAPIViews(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AvaliacoesAPIViews(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # get_queryset pega varioes elementos
    def get_queryset(self):
        if self.kwargs.get('curso_pk'): # pega o elemento 'curso_pk' do endpoint
            return self.queryset.filter(curso_id = self.kwargs.get('curso_pk'))
        return self.queryset.all()

class AvaliacaoAPIViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # get_object pega um elemento específico
    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))