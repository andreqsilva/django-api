from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer
from .permissions import IsSuperUser

# ==================== API V1 ==================== #

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
    

# ==================== API V2 ==================== #

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # Permissions:
    # AllowAny: permissão toal;
    # IsAuthenticated: somente se autenticado;
    # IsAdminUser: permissão para acessar página Django Admin
    # DjangoModelPermissions: somente se autenticado (para funções em model)

    # permission_classes = (permissions.DjangoModelPermissions,)
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions,)

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):

        # Pagination:
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id = pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes.all(), many=True)
        return Response(serializer.data)

''' VIEWSET PADRÃO    
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
'''

# VIEWSET CUSTOMIZADA: sem método list
#class AvaliacaoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
#    queryset = Avaliacao.objects.all()
#    serializer_class = AvaliacaoSerializer

class AvaliacaoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer