from rest_framework import viewsets
from core.models import *
from .serializers import *


class ArquivoViewSet(viewsets.ModelViewSet):
    queryset = Arquivo.objects.all()
    serializer_class = ArquivoSerializer


class BancaViewSet(viewsets.ModelViewSet):
    queryset = Banca.objects.all()
    serializer_class = BancaSerializer


class ContatoDocenteViewSet(viewsets.ModelViewSet):
    queryset = ContatoDocente.objects.all()
    serializer_class = ContatoDocenteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Cursodisciplina.objects.all()
    serializer_class = CursoDisciplinaSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer


class DocenteBancaViewSet(viewsets.ModelViewSet):
    queryset = Docentebanca.objects.all()
    serializer_class = DocenteBancaSerializer


class DocenteEdicaoDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Docenteedicaodisciplina.objects.all()
    serializer_class = DocenteEdicaoDisciplinaSerializer


class DocenteHabilitacaoDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Docentehabilitacaodisciplina.objects.all()
    serializer_class = DocenteHabilitacaoDisciplinaSerializer


class DocenteOrientacaoViewSet(viewsets.ModelViewSet):
    queryset = Docenteorientacao.objects.all()
    serializer_class = DocenteOrientacaoSerializer


class DocentePremioTituloViewSet(viewsets.ModelViewSet):
    queryset = Docentepremiotitulo.objects.all()
    serializer_class = DocentePremioTituloSerializer


class DocenteProducaoArtisticaViewSet(viewsets.ModelViewSet):
    queryset = Docenteproducaoartistica.objects.all()
    serializer_class = DocenteProducaoArtisticaSerializer


class DocenteProducaoBibliograficaViewSet(viewsets.ModelViewSet):
    queryset = Docenteproducaobibliografica.objects.all()
    serializer_class = DocenteProducaoBibliograficaSerializer


class DocenteProducaoTecnicaViewSet(viewsets.ModelViewSet):
    queryset = Docenteproducaobibliografica.objects.all()
    serializer_class = DocenteProducaoTecnicaSerializer


class EdicaoDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Edicaodisciplina.objects.all()
    serializer_class = EdicaoDisciplinaSerializer


class EnderecoDocenteViewSet(viewsets.ModelViewSet):
    queryset = EnderecoDocente.objects.all()
    serializer_class = EnderecoDocenteSerializer


class FuncaoParticipacaoViewSet(viewsets.ModelViewSet):
    queryset = FuncaoParticipacao.objects.all()
    serializer_class = FuncaoParticipacaoSerializer


class InstitutoViewSet(viewsets.ModelViewSet):
    queryset = Instituto.objects.all()
    serializer_class = InstitutoSerializer


class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer


class OrientacaoViewSet(viewsets.ModelViewSet):
    queryset = Orientacao.objects.all()
    serializer_class = OrientacaoSerializer


class PremioTituloViewSet(viewsets.ModelViewSet):
    queryset = Premiotitulo.objects.all()
    serializer_class = PremioTituloSerializer


class ProducaoViewSet(viewsets.ModelViewSet):
    queryset = Producao.objects.all()
    serializer_class = ProducaoSerializer


class ProducaoBibliograficaViewSet(viewsets.ModelViewSet):
    queryset = Producaobibliografica.objects.all()
    serializer_class = ProducaoBibliograficaSerializer


class ProducaoTecnicaViewSet(viewsets.ModelViewSet):
    queryset = Producaotecnica.objects.all()
    serializer_class = ProducaoTecnicaSerializer


class SituacaoOrientacaoViewSet(viewsets.ModelViewSet):
    queryset = SituacaoOrientacao.objects.all()
    serializer_class = SituacaoOrientacaoSerializer


class TipoBancaViewSet(viewsets.ModelViewSet):
    queryset = TipoBanca.objects.all()
    serializer_class = TipoBancaSerializer


class TipoContatoViewSet(viewsets.ModelViewSet):
    queryset = TipoContato.objects.all()
    serializer_class = TipoContatoSerializer


class TipoCursoViewSet(viewsets.ModelViewSet):
    queryset = TipoCurso.objects.all()
    serializer_class = TipoCursoSerializer


class TipoEnderecoViewSet(viewsets.ModelViewSet):
    queryset = TipoEndereco.objects.all()
    serializer_class = TipoEnderecoSerializer


class TipoOrientacaoViewSet(viewsets.ModelViewSet):
    queryset = TipoOrientacao.objects.all()
    serializer_class = TipoOrientacaoSerializer


class TipoProducaoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducao.objects.all()
    serializer_class = TipoProducaoSerializer


class VinculoViewSet(viewsets.ModelViewSet):
    queryset = Vinculo.objects.all()
    serializer_class = VinculoSerializer
