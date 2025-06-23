from django.urls import path, include
from rest_framework.routers import DefaultRouter


from api.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# router.register(r'bancas', BancaViewSet, basename='banca')
router.register(r'arquivos', ArquivoViewSet, basename='arquivo')
router.register(r'bancas', BancaViewSet, basename='banca')
router.register(r'contato_docentes', ContatoDocenteViewSet, basename='contato_docente')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'curso_disciplinas', CursoDisciplinaViewSet, basename='curso_disciplina')
router.register(r'departamentos', DepartamentoViewSet, basename='departamento')
router.register(r'disciplinas', DisciplinaViewSet, basename='disciplina')
router.register(r'docentes', DocenteViewSet, basename='docente')
router.register(r'docente_bancas', DocenteBancaViewSet, basename='docente_banca')
router.register(r'docente_edicao_disciplinas', DocenteEdicaoDisciplinaViewSet, basename='docente_edicao_disciplina')
router.register(r'docente_habilitacao_disciplinas', DocenteHabilitacaoDisciplinaViewSet, basename='docente_habilitacao_disciplina')
router.register(r'docente_orientacoes', DocenteOrientacaoViewSet, basename='docente_orientacao')
router.register(r'docente_premio_titulos', DocentePremioTituloViewSet, basename='docente_premio_titulo')
router.register(r'docente_producao_artisticas', DocenteProducaoArtisticaViewSet, basename='docente_producao_artistica')
router.register(r'docente_producao_bibliograficas', DocenteProducaoBibliograficaViewSet, basename='docente_producao_bibliografica')
router.register(r'docente_producao_tecnicas', DocenteProducaoTecnicaViewSet, basename='docente_producao_tecnica')
router.register(r'edicao_disciplinas', EdicaoDisciplinaViewSet, basename='edicao_disciplina')
router.register(r'endereco_docente', EnderecoDocenteViewSet, basename='endereco_docente')
router.register(r'funcao_participacoes', FuncaoParticipacaoViewSet, basename='funcao_participacao')
router.register(r'institutos', InstitutoViewSet, basename='instituto')
router.register(r'localizacoes', LocalizacaoViewSet, basename='localizacao')
router.register(r'orientacoes', OrientacaoViewSet, basename='orientacao')
router.register(r'premio_titulos', PremioTituloViewSet, basename='premio_titulo')
router.register(r'producoes', ProducaoViewSet, basename='producao')
router.register(r'producao_bibliograficas', ProducaoBibliograficaViewSet, basename='producao_bibliografica')
router.register(r'producao_tecnicas', ProducaoTecnicaViewSet, basename='producao_tecnica')
router.register(r'situacao_orientacoes', SituacaoOrientacaoViewSet, basename='situacao_orientacao')
router.register(r'tipo_bancas', TipoBancaViewSet, basename='tipo_banca')
router.register(r'tipo_contatos', TipoContatoViewSet, basename='tipo_contato')
router.register(r'tipo_cursos', TipoCursoViewSet, basename='tipo_curso')
router.register(r'tipo_enderecos', TipoEnderecoViewSet, basename='tipo_endereco')
router.register(r'tipo_orientacoes', TipoOrientacaoViewSet, basename='tipo_orientacao')
router.register(r'tipo_producoes', TipoProducaoViewSet, basename='tipo_producao')
router.register(r'vinculos', VinculoViewSet, basename='vinculo')
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),  # Inclui as URLs do router para ActionViewSet
]