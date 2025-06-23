# USP Aberta API's

O USP Aberta API Hub é um sistema desenvolvido com o framework Django, projetado para fornecer uma plataforma de
API.

## Estrutura do Projeto

O sistema está organizado nas seguintes pastas:

- **api**: Contém os scripts das REST APIs que servem o frontend.
- **core**: Armazena os modelos de dados (`core/models`), scripts de seed (`management/commands`) para popular as
  tabelas do domínio e configurações iniciais de perfis de usuários.
- **usp_aberta**: Diretório do projeto Django, incluindo as configurações do sistema.
- **usp_aberta_env**: Ambiente virtual contendo todas as dependências do projeto.

Além dessas pastas, o sistema inclui o `manage.py` e um `requirements.txt` para
gerenciamento de dependências.

## Configuração Inicial

### Pré-Requisitos

Antes de iniciar, certifique-se de ter o Python e o pip instalados em seu ambiente. O sistema foi testado com Python
3.12+ e Postgresql 14 em sistema operacional Linux.

### Configuração do Ambiente

Para configurar o ambiente e instalar as dependências necessárias, siga os passos:

1. Crie um ambiente virtual:

```bash
python -m venv usp_aberta_env
```

2. Ative o ambiente virtual:

```bash
source usp_aberta_env/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Configuração do Banco de Dados

O modelo de Sistema Gerenciador de Banco de Dados (SGBD) é Relacional e o sistema foi implantado em Postgresql 14.

- Variáveis de Ambiente: Para iniciar o sistema é necessário configurar algumas variáves de ambiente para localizar e
  acessar o banco.

    ```bash
    export USPA_DATABASE_NAME='usp_aberta_development'
    export USPA_DATABASE_USER='usp_aberta'
    export USPA_DATABASE_PASSWORD='usp_aberta'
    export USPA_DATABASE_HOST='localhost'
    ```

- Criação do banco de dados e carregamento inicial: Inicialize o banco de dados com os seguintes comandos.

    ```bash
    python manage.py makemigrations # Cria o script de migração
    python manage.py migrate # Cria o modelo físico de dados no SGBD configurado
    ```

## Uso

Para iniciar o servidor localmente, execute:

```bash
    python manage.py runserver
```

O sistema estará acessível via `http://localhost:8000/`.

## Administração

Acesse o sistema de administração do Django em `http://localhost:8000/admin` para gerenciar as tabelas do sistema.
No carregamento inicial do sistema é criado um usuaário para acessar a área administrativa admin e
senha admin.
