from django.urls import path
from .views import CursosAPIViews, CursoAPIViews, AvaliacoesAPIViews, AvaliacaoAPIViews, AvaliacaoViewSet, CursoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
# gera os endpoints automaticamente
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIViews.as_view(), name='cursos'),
    path('cursos/<int:curso_pk>', CursoAPIViews.as_view(), name='cursos'),
    path('cursos/<int:curso_pk>/avaliacoes', AvaliacoesAPIViews.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIViews.as_view(), name='curso_avaliacao'),
    path('avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIViews.as_view(), name='avaliacoes'),
    path('avaliacoes/', AvaliacoesAPIViews.as_view(), name='avaliacoes'),
]
