from django.urls import path
from .views import CursosAPIViews, CursoAPIViews, AvaliacoesAPIViews, AvaliacaoAPIViews


urlpatterns = [
    path('cursos/', CursosAPIViews.as_view(), name='cursos'),
    path('cursos/<int:pk>', CursoAPIViews.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesAPIViews.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>', AvaliacaoAPIViews.as_view(), name='avaliacoes'),
]
