from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):

    # 1. Nested Relationship
    # Registros relacionados são incluídos dentro de rcurso particular.
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # 2. HyperLinked Related Field
    # Registros, em links, dos elementos relacionados. 
    # Forma performática, recomendada para APIs REST.
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3. Primary Key Related Field
    # Registros, em PK, dos elementos relacionados.
    # Forma mais performática, ideal para casos de extremo número de registros.
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )