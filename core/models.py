# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Arquivo(models.Model):
    id_arquivo = models.IntegerField(primary_key=True, db_comment='Identificador único do arquivo (PK).')
    tamanho = models.IntegerField(db_comment='Tamanho do arquivo em bytes.')
    data_envio = models.DateField(blank=True, null=True, db_comment='Data de upload/armazenamento no sistema.')
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome original do arquivo enviado.')
    tipo = models.CharField(max_length=255, blank=True, null=True, db_comment='Tipo/MIME ou extensão do arquivo (ex: pdf, png, jpeg, docx).')
    caminho = models.CharField(max_length=255, blank=True, null=True, db_comment='Caminho de armazenamento no sistema de arquivos ou URL (se remoto).')
    id_producao = models.ForeignKey('Producao', models.DO_NOTHING, db_column='id_producao', db_comment='Referência à produção à qual o arquivo pertence (FK para producao).')

    class Meta:
        managed = False
        db_table = 'arquivo'
        db_table_comment = 'A entidade arquivo representa os arquivos digitais vinculados a uma produção acadêmica, técnica, científica ou artística. Ela permite armazenar múltiplos arquivos por produção, servindo como evidência, conteúdo complementar ou documentação comprobatória.\n\nCada registro da tabela arquivo é associado a uma entrada na entidade producao, garantindo a rastreabilidade e a organização dos materiais no sistema.'


class Banca(models.Model):
    id_banca = models.IntegerField(primary_key=True, db_comment='Identificação unica da banca')
    ano = models.IntegerField(db_comment='Ano de realização da banca.')
    data_arguicao = models.DateField(db_comment='Data em que a arguição (apresentação/defesa) ocorreu.')
    data_aprovacao = models.DateField(blank=True, null=True, db_comment='Data oficial de aprovação (pode coincidir ou não com a arguição).')
    tema = models.CharField(max_length=255, db_comment='Título ou tema do trabalho defendido.')
    observacoes = models.CharField(max_length=255, blank=True, null=True, db_comment='Campo livre para registrar considerações ou anotações adicionais.')
    id_local = models.ForeignKey('Localizacao', models.DO_NOTHING, db_column='id_local', db_comment='Local onde a banca foi montada')
    tipo = models.ForeignKey('TipoBanca', models.DO_NOTHING, db_column='tipo', db_comment='Tipo de banca  ex: TCC, Mestrado, Doutorado,Qualificação (M/D)')

    class Meta:
        managed = False
        db_table = 'banca'
        db_table_comment = 'A entidade banca representa comissões avaliadoras formadas para acompanhar e julgar trabalhos acadêmicos, como defesas de TCC, dissertações ou teses. Cada banca é composta por docentes com diferentes funções (presidente, membro, suplente) e está associada a um tema, a uma data de arguição e, quando aplicável, à data de aprovação.'


class ContatoDocente(models.Model):
    id_docente = models.ForeignKey('Docente', models.DO_NOTHING, db_column='id_docente', db_comment='Docente do contato')
    valor = models.CharField(max_length=255, db_comment='Valor atribuido ao contato, por exemplo se for email: email@email.com ou telefone 9999-99999')
    observacao = models.TextField(blank=True, null=True, db_comment='Observações gerais do contato')
    tipo_contato = models.ForeignKey('TipoContato', models.DO_NOTHING, db_column='tipo_contato', db_comment='Tipo do contato, por ex: email, telefone.')
    id_contato = models.IntegerField(primary_key=True, db_comment='Identificação unica do contato')

    class Meta:
        managed = False
        db_table = 'contato_docente'
        db_table_comment = 'Contatos de um docente, por ex: email, telefone'


class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True, db_comment='Identificação do curso')
    nome = models.CharField(max_length=255, db_comment='Nome do curso')
    area_conhecimento = models.CharField(max_length=255, blank=True, null=True, db_comment='Area de conhecimento')
    id_instituto = models.ForeignKey('Instituto', models.DO_NOTHING, db_column='id_instituto', db_comment='Instituto a que pertence o curso')
    tipo = models.ForeignKey('TipoCurso', models.DO_NOTHING, db_column='tipo', db_comment='Tipo de curso que é oferecido')

    class Meta:
        managed = False
        db_table = 'curso'
        db_table_comment = 'A entidade curso representa uma estrutura acadêmica formal oferecida pela Universidade, composta por um conjunto organizado de disciplinas que definem sua grade curricular. Cada curso é associado a uma área do conhecimento, a um tipo (como bacharelado, licenciatura, tecnólogo, especialização etc.) e está vinculado a um instituto ou unidade de ensino responsável por sua oferta.\n\nOs cursos são definidos por:\n\t•\tNome e tipo do curso\n\t•\tÁrea do conhecimento\n\t•\tInstituição de origem (ex: Instituto ou Departamento)\n\t•\tDisciplinas obrigatórias e optativas\n\t•\tEstrutura curricular por fases, semestres ou módulos'


class Cursodisciplina(models.Model):
    id_curso = models.OneToOneField(Curso, models.DO_NOTHING, db_column='id_curso', primary_key=True, db_comment='Qual é o curso na grade')  # The composite primary key (id_curso, id_disciplina) found, that is not supported. The first column is selected.
    id_disciplina = models.ForeignKey('Disciplina', models.DO_NOTHING, db_column='id_disciplina', db_comment='Disciplina oferecida pelo curso')
    obrigatoria = models.BooleanField(blank=True, null=True, db_comment='Se é uma disciplina obrigatória no curso')
    semestre_ideal = models.IntegerField(blank=True, null=True, db_comment='Qual é o semestre ideal que a matéria é ofereciada')

    class Meta:
        managed = False
        db_table = 'cursodisciplina'
        unique_together = (('id_curso', 'id_disciplina'),)
        db_table_comment = 'A associação entre curso e disciplina permite compor a matriz curricular, definindo quais disciplinas são obrigatórias, em que fase são ofertadas, e suas características específicas dentro do contexto do curso.'


class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True, db_comment='Identificação única do departamento')
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome  do departamento')
    sigla = models.CharField(max_length=255, blank=True, null=True, db_comment='Siga do departamento')
    chefe = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do chefe do departamento')
    vice_chefe = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do vice chefe do departamento')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição e finalidade do departamento')
    endereco = models.CharField(max_length=255, blank=True, null=True, db_comment='Enderço interno do departamento')
    numero_docentes = models.IntegerField(blank=True, null=True, db_comment='Número de docentes do departamento')
    ano_fundacao = models.IntegerField(blank=True, null=True, db_comment='Ano de fundação do departamento')
    id_instituto = models.ForeignKey('Instituto', models.DO_NOTHING, db_column='id_instituto', db_comment='Instituto que pertence o departamento')

    class Meta:
        managed = False
        db_table = 'departamento'
        db_table_comment = 'A entidade departamento representa uma subunidade acadêmica vinculada a um instituto, responsável por coordenar atividades de ensino, pesquisa e extensão em áreas específicas do conhecimento. Armazena informações administrativas e acadêmicas como nome, sigla, descrição institucional, endereço interno, número de docentes, ano de fundação e a chefia atual.\n\nCada departamento está diretamente associado a um instituto, do qual herda sua estrutura organizacional e participa da oferta de cursos, disciplinas e da alocação de docentes.'


class Disciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True, db_comment='Identificação da disciplina')
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome da disciplina')
    sigla = models.CharField(blank=True, null=True, db_comment='Sigla de indentificação da disciplina')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do conteúdo da disciplina')
    carga_horaria = models.IntegerField(blank=True, null=True, db_comment='Carga horária atribuida a disciplina')
    creditos = models.IntegerField(blank=True, null=True, db_comment='Quando créditos a matéria oferece')
    idioma = models.CharField(max_length=255, blank=True, null=True, db_comment='Idioma que é oferecido a disciplina')
    modalidade = models.CharField(max_length=255, blank=True, null=True, db_comment='Qual é a modealidade do oferecimento, por exemplo: presencial, online, híbrido')
    link_jupiter = models.CharField(max_length=255, blank=True, null=True, db_comment='Url para o sistema de apoio a matricula da USP')

    class Meta:
        managed = False
        db_table = 'disciplina'
        db_table_comment = 'A entidade disciplina representa o cadastro básico e estruturado das disciplinas oferecidas pela Universidade. Ela funciona como referência central para todos os oferecimentos curriculares, reunindo as informações essenciais e perenes que caracterizam cada componente curricular.\n\nCada registro de disciplina inclui dados como:\n\t•\tNome e sigla identificadora\n\t•\tEmenta e descrição geral do conteúdo (descrita no link do jupterweb)\n\t•\tCarga horária total e número de créditos\n\t•\tModalidade (presencial, online, híbrida)\n\t•\tIdioma de instrução, quando aplicável\n\nEssa entidade não está vinculada a um período específico, servindo como base para os múltiplos oferecimentos semestrais, modelados separadamente pela entidade edição de disciplina.'


class Docente(models.Model):
    id_docente = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, db_comment='Nome do docente')
    genero = models.CharField(blank=True, null=True, db_comment='Genero definido pelo docente')
    raca = models.CharField(max_length=255, blank=True, null=True, db_comment='Raça definida pelo docente')
    nascimento = models.DateField(db_comment='data de nascimento')
    palavras_chave = models.TextField(blank=True, null=True, db_comment='Palavras que chaves usandas na busca para selecionar o docente')
    id_departamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_departamento', blank=True, null=True, db_comment='Departamento que esta alocado')

    class Meta:
        managed = False
        db_table = 'docente'
        db_table_comment = 'A entidade docente representa os professores vinculados à Universidade, responsáveis por atividades de ensino, pesquisa, orientação, participação em bancas e produção acadêmica. Ela armazena os dados essenciais para identificação, caracterização e relacionamento dos docentes com os demais elementos do sistema acadêmico.\n\nEntre os atributos armazenados estão informações pessoais, acadêmicas e institucionais, tais como nome, gênero, raça, data de nascimento, palavras-chave de atuação e vínculo com o departamento de origem.\n\nEssa entidade é central no modelo, sendo relacionada a disciplinas, orientações, produções, bancas, cursos e outras estruturas institucionais.'


class Docentebanca(models.Model):
    id_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='id_docente', primary_key=True, db_comment='Identificação do docente')  # The composite primary key (id_docente, id_banca) found, that is not supported. The first column is selected.
    id_banca = models.ForeignKey(Banca, models.DO_NOTHING, db_column='id_banca', db_comment='Detalhes da banca')
    vinculo = models.ForeignKey('Vinculo', models.DO_NOTHING, db_column='vinculo', db_comment='Qual é o vículo com essa banca que o docente exerceu, por exemplo: presidente, avaliador, suplente, etc.')

    class Meta:
        managed = False
        db_table = 'docentebanca'
        unique_together = (('id_docente', 'id_banca'),)
        db_table_comment = 'Bancas que um docente participou'


class Docenteedicaodisciplina(models.Model):
    id_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='id_docente', primary_key=True, db_comment='Docente que participa da disciplina')  # The composite primary key (id_docente, id_edicao) found, that is not supported. The first column is selected.
    id_edicao = models.ForeignKey('Edicaodisciplina', models.DO_NOTHING, db_column='id_edicao', db_comment='Edição da matéria oferecida')
    carga_horaria_ministrada = models.IntegerField(blank=True, null=True, db_comment='Carga horária desse ofereciemnto em específico')
    vinculo = models.ForeignKey('Vinculo', models.DO_NOTHING, db_column='vinculo', db_comment='Tipo de vículo que o docente possui com a disciplica oferecida')

    class Meta:
        managed = False
        db_table = 'docenteedicaodisciplina'
        unique_together = (('id_docente', 'id_edicao'),)
        db_table_comment = 'A disciplina é ofertada por edição (semestre/ano/turma), assim um docente pode ficar vinculado as edições das disciplina que já participou. Uma disciplina pode ser mistrada por vários docentes.'


class Docentehabilitacaodisciplina(models.Model):
    id_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='id_docente', primary_key=True, db_comment='Docente que pode participar desta disciplina')  # The composite primary key (id_docente, id_disciplina) found, that is not supported. The first column is selected.
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina', db_comment='Disciplina oferecida pelo curso')

    class Meta:
        managed = False
        db_table = 'docentehabilitacaodisciplina'
        unique_together = (('id_docente', 'id_disciplina'),)
        db_table_comment = 'Os docentes são associados somente as disciplinas que estão aptos a lecionar'


class Docenteorientacao(models.Model):
    id_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='id_docente', primary_key=True, db_comment='Docente responsável pela orientação')  # The composite primary key (id_docente, id_orientacao) found, that is not supported. The first column is selected.
    id_orientacao = models.ForeignKey('Orientacao', models.DO_NOTHING, db_column='id_orientacao', db_comment='Detalhes da orientação')
    vinculo = models.ForeignKey('Vinculo', models.DO_NOTHING, db_column='vinculo', db_comment='Tipo de vinculo que o docente tem na orientação, por exemplo orientador, coordenador, coorentador, etc.')

    class Meta:
        managed = False
        db_table = 'docenteorientacao'
        unique_together = (('id_docente', 'id_orientacao'),)
        db_table_comment = 'Orientações de um docente'


class Docentepremiotitulo(models.Model):
    id_docente = models.OneToOneField(Docente, models.DO_NOTHING, db_column='id_docente', primary_key=True, db_comment='Docente que recebe o prêmio')  # The composite primary key (id_docente, id_premio_titulo) found, that is not supported. The first column is selected.
    id_premio_titulo = models.ForeignKey('Premiotitulo', models.DO_NOTHING, db_column='id_premio_titulo', db_comment='Prêmio recebido pelo docente.')
    data_recebimento = models.DateField(blank=True, null=True, db_comment='Data de recebimento do prêmio. É possível que o prêmio seja entregue em datas distintas quando o prêmio é compartilhado.')

    class Meta:
        managed = False
        db_table = 'docentepremiotitulo'
        unique_together = (('id_docente', 'id_premio_titulo'),)
        db_table_comment = 'Um prêmio pode ser dado a vários docentes'


class Docenteproducaoartistica(models.Model):
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', db_comment='Participação do docente na produção artisitica')
    id_producao = models.ForeignKey('Producao', models.DO_NOTHING, db_column='id_producao', db_comment='Id de referência da gereneralização, pois essa entidade é uma especialização.')

    class Meta:
        managed = False
        db_table = 'docenteproducaoartistica'
        db_table_comment = 'Uma produção artistica pode ter vários autores'


class Docenteproducaobibliografica(models.Model):
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', db_comment='id de assoação com o docente')
    vinculo = models.ForeignKey('Vinculo', models.DO_NOTHING, db_column='vinculo', db_comment='tipo de participação que o docente tem na produção científica')
    id_producao = models.ForeignKey('Producaobibliografica', models.DO_NOTHING, db_column='id_producao', db_comment='Id de associação com a produção')

    class Meta:
        managed = False
        db_table = 'docenteproducaobibliografica'
        db_table_comment = 'Produção científica dos docentes'


class Docenteproducaotecnica(models.Model):
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', db_comment='id de associação com o docente')
    funcao_participacao = models.ForeignKey('FuncaoParticipacao', models.DO_NOTHING, db_column='funcao_participacao', blank=True, null=True, db_comment='id da associação com o tipo de função que o docente tem com a produção técnica')
    id_producao = models.ForeignKey('Producaotecnica', models.DO_NOTHING, db_column='id_producao', db_comment='Id de associação com a produção')

    class Meta:
        managed = False
        db_table = 'docenteproducaotecnica'
        db_table_comment = 'Uma produção técnica pode ser desenvolvida em parcerias com outras pessoas'


class Edicaodisciplina(models.Model):
    id_edicao = models.IntegerField(primary_key=True, db_comment='Identifcação do oferecimento')
    id_disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disciplina', db_comment='Qual é a disciplina que trata esse oferecimento')
    ano = models.IntegerField(blank=True, null=True, db_comment='Ano em que esta sendo oferecida a disciplina')
    semestre = models.CharField(blank=True, null=True, db_comment='Semestre de oferencimento')
    numero_alunos = models.IntegerField(blank=True, null=True, db_comment='Número de alunos matriculados na disciplina')
    link_avaliacao = models.CharField(blank=True, null=True, db_comment='Link para o sistema e-disciplina, ou outro sistema onde estão resgistrada as notas')
    id_local = models.ForeignKey('Localizacao', models.DO_NOTHING, db_column='id_local', blank=True, null=True, db_comment='Local de oferecimento da disciplina')

    class Meta:
        managed = False
        db_table = 'edicaodisciplina'
        db_table_comment = 'Uma edição de disciplina representa o oferecimento concreto de uma disciplina em um determinado semestre e ano letivo, podendo ainda estar associada a uma turma específica. Essa edição está vinculada à disciplina base, que funciona como um cadastro genérico e perene contendo as informações estruturais da disciplina — como nome, sigla, ementa, carga horária e créditos.\n\nA edição, por sua vez, contém os dados variáveis e contextuais do oferecimento, tais como:\n\t•\tPeríodo letivo (ano e semestre)\n\t•\tNúmero de alunos matriculados\n\t•\tLocal de realização\n\t•\tDocentes responsáveis\n\t•\tLinks para sistema acadêmico ou avaliações\n\nEsse modelo permite distinguir a identidade estável da disciplina de suas múltiplas implementações ao longo do tempo.'


class EnderecoDocente(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente')
    logradouro = models.CharField(max_length=255, db_comment='Rua, avenida, etc')
    numero = models.CharField(max_length=50, blank=True, null=True, db_comment='Número do endereço, é um varchar pois pode ser S/N.')
    complemento = models.CharField(max_length=100, blank=True, null=True, db_comment='Complemento do endereço')
    bairro = models.CharField(max_length=255, blank=True, null=True, db_comment='Bairro do endereço')
    cidade = models.CharField(max_length=255, db_comment='Cidade do endereço')
    estado = models.CharField(max_length=255, db_comment='Estado do endereço')
    cep = models.CharField(max_length=10, blank=True, null=True, db_comment='CEP do endereço')
    pais = models.CharField(max_length=255, blank=True, null=True, db_comment='País do endereço')
    observacao = models.TextField(blank=True, null=True, db_comment='Observações sobre o endereço do docente')
    tipo_endereco = models.ForeignKey('TipoEndereco', models.DO_NOTHING, db_column='tipo_endereco', blank=True, null=True, db_comment='Tipo de endereço: comercial, residencial, temporário, etc.')

    class Meta:
        managed = False
        db_table = 'endereco_docente'
        db_table_comment = 'Endereço do docente'


class FuncaoParticipacao(models.Model):
    funcao_participacao = models.CharField(unique=True, max_length=50, blank=True, null=True, db_comment='Nome da fução, é chave primária')
    descricao = models.CharField(max_length=255, blank=True, null=True, db_comment='Descrição das contribuições dadas pelo participante.')

    class Meta:
        managed = False
        db_table = 'funcao_participacao'
        db_table_comment = 'Cada autor do documento técnico pode ter uma participação específica na elabaoração do documento, por exemplo:\nautor_principal: Criador principal da versão\ncoautor: Contribuição relevante, mas secundária\nrevisor: Revisão técnica ou textual\nresponsavel_design: Autor da parte gráfica ou layout\ndesenvolvedor: Se a produção for um software\nconsultor: Contribuição externa, não autoral'


class Instituto(models.Model):
    id_instituto = models.IntegerField(primary_key=True, db_comment='Identificação unica do instituto')
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do instituto')
    numero_docentes = models.IntegerField(blank=True, null=True, db_comment='Número mas recente de docentes  do instituto')
    ano_fundacao = models.IntegerField(blank=True, null=True, db_comment='Ano de fundação  do instituto')
    numero_alunos = models.IntegerField(blank=True, null=True, db_comment='Número de alunos  do instituto')
    diretor = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do diretor  do instituto')
    vice_diretor = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do  vice diretor do instituto')
    site = models.CharField(max_length=255, blank=True, null=True, db_comment='Url  do instituto')
    id_local = models.ForeignKey('Localizacao', models.DO_NOTHING, db_column='id_local', db_comment='Local do instituto')

    class Meta:
        managed = False
        db_table = 'instituto'
        db_table_comment = 'A entidade instituto representa uma unidade acadêmica da Universidade, responsável pela oferta de cursos, disciplinas e pela vinculação de docentes e departamentos. Armazena informações institucionais  como nome, número de docentes e alunos, ano de fundação, direção atual, site institucional e localização física (referenciada pela entidade local).\n\nEssa entidade serve como ponto de origem organizacional para a estrutura acadêmica e administrativa do sistema.'


class Localizacao(models.Model):
    id_local = models.IntegerField(primary_key=True, db_comment='Identificação unica do local')
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome dado ao local')
    localizacao = models.CharField(max_length=255, blank=True, null=True, db_comment='A localização pode um endereço ou um local virtual')
    idade = models.IntegerField(blank=True, null=True, db_comment='Quando é um local físico pode ser interessante fazer a idade do local')
    data_ultima_reforma = models.DateField(blank=True, null=True, db_comment='Se for um local físico existe informações sobre a ultima reforma')
    numero_salas = models.IntegerField(blank=True, null=True, db_comment='Quantidade de salas do local físico ou virtual')
    numero_blocos = models.IntegerField(blank=True, null=True, db_comment='Númro de blocos do local físico')

    class Meta:
        managed = False
        db_table = 'localizacao'
        db_table_comment = 'A localização representa um local físico ou lógico (como um ambiente virtual)'


class Orientacao(models.Model):
    id_orientacao = models.IntegerField(primary_key=True, db_comment='identificação da orientação')
    tipo = models.ForeignKey('TipoOrientacao', models.DO_NOTHING, db_column='tipo', db_comment='Tipo de orientação que podem ser de mestrado, doutorado, tcc, etc.')
    ano = models.IntegerField(blank=True, null=True, db_comment='Ano que em se iniciou a orientação')
    situacao = models.ForeignKey('SituacaoOrientacao', models.DO_NOTHING, db_column='situacao', db_comment='Situação do andamento da orientação que pode ser em andamento, concluída, etc.')
    nome_orientado = models.CharField(max_length=255, db_comment='Nome do orientado')
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', db_comment='Curso que esta associado a orientação')
    data_inicio = models.DateField(db_comment='Data que se iniciou a orientação')
    data_fim = models.DateField(blank=True, null=True, db_comment='Data de finalização da orientação')
    observacoes = models.TextField(blank=True, null=True, db_comment='Observações gerais sobre a orientação')
    titulo_trabalho = models.CharField(max_length=255, blank=True, null=True, db_comment='Titulo do trabalho desenvolvido')

    class Meta:
        managed = False
        db_table = 'orientacao'
        db_table_comment = 'A entidade orientação registra o vínculo entre docentes e estudantes em projetos acadêmicos orientados, como trabalhos de conclusão de curso, dissertações de mestrado ou teses de doutorado. Cada orientação possui um tipo (TCC, mestrado, doutorado etc.), tema, período de vigência e situação atual (em andamento, concluída, cancelada).'


class Premiotitulo(models.Model):
    id_premio_titulo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do prêmio')
    ano = models.IntegerField(blank=True, null=True, db_comment='Ano do prêmio dado a docentes')

    class Meta:
        managed = False
        db_table = 'premiotitulo'
        db_table_comment = 'Prêmios recebidos pelos docentes'


class Producao(models.Model):
    id_producao = models.OneToOneField('Producaobibliografica', models.DO_NOTHING, db_column='id_producao', primary_key=True)
    descricao = models.TextField(db_comment='Descrição da produção')
    ano = models.IntegerField(db_comment='Ano em que foi criado a produção.')
    data_producao = models.DateField(blank=True, null=True, db_comment='Data de finalização ou catalogação da produção.')
    observacao = models.TextField(blank=True, null=True, db_comment='Observações')
    nome = models.CharField(max_length=255, db_comment='Nome da produção')
    titulo = models.CharField(max_length=255, db_comment='Título da produção')
    tipo = models.ForeignKey('TipoProducao', models.DO_NOTHING, db_column='tipo', db_comment='Tipo de produção')

    class Meta:
        managed = False
        db_table = 'producao'
        db_table_comment = 'A entidade produção representa uma generalização dos diversos tipos de trabalhos desenvolvidos pelos docentes no âmbito acadêmico e profissional. Essa estrutura unificada permite organizar e rastrear todas as formas de produção realizadas por um docente, sejam elas de natureza científica, técnica ou artística.\n\nCada produção é vinculada a um docente (ou a vários, em coautoria), e pode assumir diferentes especializações, como:\n\t•\tProdução Bibliográfica: artigos, livros, capítulos, resumos, etc.\n\t•\tProdução Técnica: softwares, relatórios, projetos, patentes, etc.\n\t•\tProdução Artística: obras plásticas, exposições, performances, etc.\n\nA entidade genérica producao reúne os campos comuns (como título, ano, tipo, vinculação ao docente), enquanto as entidades especializadas estendem essas informações com atributos específicos conforme o tipo da produção.\n\nEssa abordagem favorece:\n\t•\tReutilização de estrutura e consultas unificadas;\n\t•\tFlexibilidade para incluir novos tipos de produção;\n\t•\tAdoção de herança em modelagem orientada a objetos ou estruturas EER.'


class Producaobibliografica(models.Model):
    issn_isbn = models.CharField(max_length=255, blank=True, null=True, db_comment='Número identificador da obra (ISSN para periódicos, ISBN para livros).')
    nome_periodico = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome do periódico, revista ou veículo de publicação.')
    volume = models.CharField(max_length=255, blank=True, null=True, db_comment='Volume ou coleção em que a produção foi publicada.')
    numero = models.CharField(max_length=255, blank=True, null=True, db_comment='Número do volume ou edição.')
    doi = models.CharField(max_length=255, blank=True, null=True, db_comment='DOI (Digital Object Identifier) da publicação, quando disponível.')
    data_publicacao = models.DateField(blank=True, null=True, db_comment='Data de publicação oficial.')
    id_producao = models.IntegerField(unique=True, db_comment='Id de referência da gereneralização, pois essa entidade é uma especialização.')
    paginas = models.IntegerField(blank=True, null=True, db_comment='Quantidade de páginas publicadas.')
    local_publicacao = models.CharField(max_length=255, blank=True, null=True, db_comment='Cidade, estado ou país da publicação.')
    editora = models.CharField(max_length=255, blank=True, null=True, db_comment='Nome da editora responsável pela publicação.')

    class Meta:
        managed = False
        db_table = 'producaobibliografica'
        db_table_comment = 'A entidade producaobibliografica representa uma especialização da entidade genérica produção, destinada ao registro das produções científicas realizadas por docentes da Universidade. Ela abrange publicações acadêmicas como artigos em periódicos, capítulos de livros, livros completos, resumos em anais de eventos, editoriais, entre outros.\n\nAlém dos campos herdados da entidade producao (como título, tipo, ano e vínculo com docentes), a producaobibliografica adiciona um conjunto de atributos específicos para descrever com precisão os dados bibliográficos da publicação:'


class Producaotecnica(models.Model):
    versao = models.CharField(blank=True, null=True, db_comment='Versão da produção técnica v1, v2, final')
    id_producao_anterior = models.IntegerField(blank=True, null=True, db_comment='Id de referência de onde foi derivada a versão, é uma auto referência.')
    id_producao = models.IntegerField(unique=True, blank=True, null=True, db_comment='Id de referência da gereneralização, pois essa entidade é uma especialização.')

    class Meta:
        managed = False
        db_table = 'producaotecnica'
        db_table_comment = 'A entidade produção técnica representa o registro e a catalogação das produções de natureza técnica desenvolvidas por docentes da Universidade, como softwares, relatórios, manuais, protótipos, serviços técnicos, entre outros.\n\nCada produção técnica pode possuir várias versões, permitindo rastrear a evolução do conteúdo ao longo do tempo. O modelo adota uma estrutura de versionamento encadeado, onde:\n\t•\tCada versão aponta para a versão anterior da qual foi derivada (id_versao_anterior);\n\t•\tA primeira versão possui esse campo nulo;\n\t•\tQuando uma versão é derivada, ela herda o conteúdo da versão anterior, que passa a ser imutável no sistema;\n\t•\tTodas as alterações posteriores devem ser feitas na nova versão, garantindo o histórico de modificações e a rastreabilidade.\n\nEssa abordagem oferece:\n\t•\tControle de integridade e rastreamento das alterações;\n\t•\tSuporte a múltiplos autores em cada versão, com papéis distintos (ex: desenvolvedor, editor, responsável técnico);\n\t•\tPossibilidade de vincular cada versão a métricas específicas, avaliações ou registros legais (como INPI, ISBN, DOI etc.).'


class SituacaoOrientacao(models.Model):
    situacao = models.CharField(primary_key=True, db_comment='Identificação da situação da orientação')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição e finalidade da orientação')

    class Meta:
        managed = False
        db_table = 'situacao_orientacao'
        db_table_comment = 'Uma orientação possui estagios de acompanhamento, por exemplo:\nandamento: Orientação em andamento\nconcluida: Orientação concluída com sucesso\ncancelada: Orientação cancelada ou interrompida\nsuspensa: Orientação temporariamente suspensa'


class TipoBanca(models.Model):
    tipo = models.CharField(primary_key=True, max_length=255, db_comment='Tipo de banca (ex: TCC, Mestrado, Doutorado,Qualificação (M/D)).')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do tipo de banca e finalidade')

    class Meta:
        managed = False
        db_table = 'tipo_banca'
        db_table_comment = 'Tipo de banca que o docente participa'


class TipoContato(models.Model):
    tipo_contato = models.CharField(primary_key=True, max_length=255, db_comment='Nome do tipo de contato, por ex: email, telefone')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do tipo de contato')

    class Meta:
        managed = False
        db_table = 'tipo_contato'
        db_table_comment = 'Tipo de contato do docente.'


class TipoCurso(models.Model):
    tipo = models.CharField(primary_key=True, max_length=255, db_comment='Nome do tipo de curso')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do curso oferecido')

    class Meta:
        managed = False
        db_table = 'tipo_curso'
        db_table_comment = 'Tipo de curso que pode ser regular, de versão, de pós, etc.'


class TipoEndereco(models.Model):
    tipo_endereco = models.CharField(primary_key=True, max_length=50, db_comment='Chave primária do tipo de endereço: residencial, comercial, etc.')
    descricao = models.CharField(max_length=255, blank=True, null=True, db_comment='Descrição do tipo de endereço')

    class Meta:
        managed = False
        db_table = 'tipo_endereco'
        db_table_comment = 'Tipo de endereço que o docente pode esta associado, por ex:\nComercial\nResidêncial\nTemporário'


class TipoOrientacao(models.Model):
    tipo = models.CharField(primary_key=True, max_length=255, db_comment='Nome do tipo de orientação, ex: tcc, mestrado, doutorado, etc.')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição e finalidade do tipo de orientação')

    class Meta:
        managed = False
        db_table = 'tipo_orientacao'
        db_table_comment = 'Tipo de orientação que o docente participa, por ex:\ntcc: Trabalho de Conclusão de Curso\nmestrado: Dissertação de Mestrado\ndoutorado: Tese de Doutorado\niniciacao: Iniciação Científica\nposdoc: Pós-Doutorado\nespecializacao: Monografia de Especialização'


class TipoProducao(models.Model):
    tipo = models.CharField(primary_key=True, max_length=255, db_comment='Tipo de produção')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do objetivo do documento técnico.')

    class Meta:
        managed = False
        db_table = 'tipo_producao'
        db_table_comment = 'Tipo de produção desenvolvida pelos docentes:\nPara documentos científicos:\nartigo_periodico: Artigo em periódico\nartigo_evento: Artigo em anais de evento\nlivro: Livro completo\ncapitulo_livro: Capítulo de livro\nresumo_expandido: Resumo expandido\nresumo_simples: Resumo simples\neditorial: Editorial\noutro: Outro tipo de produção\n\n\nPara documentos técnicos:\nsoftware: Desenvolvimento de sistemas ou aplicações.\nrelatorio_tecnico: Documentos técnicos, pareceres ou relatórios institucionais.\nmanual_tecnico: Guias de uso ou operação de equipamentos, sistemas ou processos.\npatente: Pedido ou concessão de patente técnica ou de invenção.\nregistro_programa: Registro oficial de programas de computador (ex: INPI).\nprototipo: Construção de protótipos funcionais ou conceituais.\nprojeto_tecnico: Projeto de engenharia, arquitetura, computação, etc.\nmaquete: Representações físicas ou virtuais de projetos técnicos.\ndesenho_industrial: Criação de design técnico aplicado à indústria.\ndesenvolvimento_material_didatico: Produção de conteúdo técnico com fins educacionais.\ndesenvolvimento_multimidia: Jogos, vídeos interativos, animações técnicas.\neditoração_tecnica: Coordenação técnica de periódicos, livros ou materiais.\nparecer_tecnico: Avaliação formal técnica sobre projetos, produtos ou serviços.\naplicativo_mobile: Aplicações técnicas desenvolvidas para dispositivos móveis.\nbase_dados: Estruturas organizadas de dados técnicos, estatísticos ou científicos.\nservico_tecnico_especializado: Atividades técnicas prestadas como consultoria ou assessoria.\noutro: Produções técnicas não classificadas acima.\n\nPara arte:\nArte contemporânea\nArte clássica\nArte de rua'


class Vinculo(models.Model):
    vinculo = models.CharField(primary_key=True, max_length=255, db_comment='Nome do vículo que chave primária')
    descricao = models.TextField(blank=True, null=True, db_comment='Descrição do vínculo')

    class Meta:
        managed = False
        db_table = 'vinculo'
        db_table_comment = 'Os docentes podem assumir diferentes formas de participação em diversas atividades acadêmicas, como produções técnicas e bibliográficas, orientações, bancas examinadoras e disciplinas lecionadas. Esta entidade centraliza os tipos de vínculo existentes entre o docente e os elementos do sistema em que ele atua, permitindo a padronização e reutilização desses papeis em diferentes contextos.\n\nA seguir, são apresentados exemplos de tipos de vínculo organizados por escopo:\n\nPara banca:\npresidente\nmembro\nsuplente\navaliador externo\norientador (caso a banca inclua o orientador formalmente)\nrelator (se aplicável em dissertações/tese)\n\nPara orientação:\norientador\ncoorientador\n\nPara produção bibliografica:\n autor\n coautor\n organizador\n editor técnico\n tradutor\n\nPara docente na disciplina:\nministrante\ncoordenador\nauxiliar'
