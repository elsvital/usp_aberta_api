from rest_framework import serializers
from core.models import *

class DocenteProducaoSerializer(serializers.ModelSerializer):
    producoes_bibliograficas = serializers.SerializerMethodField()
    producoes_artistica = serializers.SerializerMethodField()
    producoes_tecnicas = serializers.SerializerMethodField()

    class Meta:
        model = Docente
        fields = '__all__'  # ou liste os campos manualmente
        depth = 1

    def get_producoes_bibliograficas(self, obj):
        relacoes = Docenteproducaobibliografica.objects.filter(id_docente=obj.id_docente)
        ids_producoes = relacoes.values_list('id_producao', flat=True)
        producoes = Producaobibliografica.objects.filter(id_producao__in=ids_producoes)
        return ProducaoSerializer(producoes, many=True).data

    def get_producoes_tecnicas(self, obj):
        relacoes = Docenteproducaotecnica.objects.filter(id_docente=obj.id_docente)
        ids = relacoes.values_list('id_producao', flat=True)
        producoes = Producaotecnica.objects.filter(id_producao__in=ids)
        return ProducaoSerializer(producoes, many=True).data

    def get_producoes_artisticas(self, obj):
        ids = Docenteproducaoartistica.objects.filter(
            id_docente=obj.id_docente
        ).values_list('id_producao', flat=True)
        producoes = Producao.objects.filter(id_producao__in=ids)
        return ProducaoSerializer(producoes, many=True).data

class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arquivo
        fields = '__all__'


class BancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banca
        fields = '__all__'


class ContatoDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContatoDocente
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class CursoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursodisciplina
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'


class DocenteBancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentebanca
        fields = '__all__'


class DocenteEdicaoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docenteedicaodisciplina
        fields = '__all__'


class DocenteHabilitacaoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentehabilitacaodisciplina
        fields = '__all__'


class DocenteOrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docenteorientacao
        fields = '__all__'


class DocentePremioTituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentepremiotitulo
        fields = '__all__'


class DocenteProducaoArtisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docenteproducaoartistica
        fields = '__all__'


class DocenteProducaoBibliograficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docenteproducaobibliografica
        fields = '__all__'


class DocenteProducaoTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docenteproducaotecnica
        fields = '__all__'


class EdicaoDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edicaodisciplina
        fields = '__all__'


class EnderecoDocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoDocente
        fields = '__all__'


class FuncaoParticipacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncaoParticipacao
        fields = '__all__'


class InstitutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituto
        fields = '__all__'


class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'


class OrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacao
        fields = '__all__'


class PremioTituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premiotitulo
        fields = '__all__'


class ProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producao
        fields = '__all__'


class ProducaoBibliograficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producaobibliografica
        fields = '__all__'


class ProducaoTecnicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producaotecnica
        fields = '__all__'


class SituacaoOrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituacaoOrientacao
        fields = '__all__'


class TipoBancaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBanca
        fields = '__all__'


class TipoContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContato
        fields = '__all__'


class TipoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCurso
        fields = '__all__'


class TipoEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEndereco
        fields = '__all__'


class TipoOrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoOrientacao
        fields = '__all__'


class TipoProducaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducao
        fields = '__all__'


class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = '__all__'
