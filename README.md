# learning-fastapi

[![Python Version](https://img.shields.io/badge/python-3.11.9-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3119/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.2-60A5FA?logo=python)](https://python-poetry.org/)
[![License](https://img.shields.io/github/license/LoboProgrammingg/FastAPI?color=brightgreen)](LICENSE)
[![Build status](https://img.shields.io/badge/test-passing-brightgreen?logo=pytest&logoColor=white)](#testes)
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen)](#testes)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-0B3D91?logo=python)](https://docs.astral.sh/ruff/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](#status-do-projeto)

---

<div align="center">

> 💡 Este projeto está em desenvolvimento e poderá receber atualizações frequentes, melhorias e ajustes. Acompanhe para não perder novidades!

</div>

---

## Indice

- [Setup rapido](#setup-rapido)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Dependencias principais](#dependencias-principais)
- [Tasks automatizadas taskipy](#tasks-automatizadas-taskipy)
- [Como rodar o projeto](#como-rodar-o-projeto)
- [Testes](#testes)
- [Documentacao](#documentacao)
- [Boas praticas adotadas](#boas-praticas-adotadas)
- [Dicas interativas e links uteis](#dicas-interativas-e-links-uteis)
- [Autor](#autor)
- [Licenca](#licenca)

---

## Setup rapido

<details>
<summary><strong>Mostrar instrucoes detalhadas</strong></summary>

### 1. Instale dependencias do sistema

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```

### 2. Instale o pyenv

```bash
curl https://pyenv.run | bash
```

Adicione ao seu shell (`.bashrc`, `.zshrc`...):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"
```
> Para Zsh, use `~/.zshrc`.

### 3. Instale e defina o Python

```bash
pyenv install 3.11.9
pyenv global 3.11.9
python --version # Deve retornar Python 3.11.9
```

### 4. Instale pipx e Poetry

```bash
sudo apt install pipx
pipx install poetry
pipx ensurepath
```
> Reinicie o terminal se necessario.

### 5. Configure o projeto

```bash
pyenv local 3.11.9
poetry install
```
</details>

---

## Estrutura do projeto

```text
learning-fastapi/
├── src/
│   └── learning_fastapi/
│       ├── __init__.py
│       ├── app.py
│       ├── models.py
│       ├── schemas.py
│       ├── database.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_db.py
│   ├── test_app.py
│   └── conftest.py
├── .python-version
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── poetry.lock
├── mkdocs.yml
├── README.md
└── ...
```

- **src/**: Codigo-fonte do app
- **tests/**: Testes automatizados
- **pyproject.toml**: Configuracao do projeto e dependencias

---

## Dependencias principais

- [`fastapi[standard]`](https://fastapi.tiangolo.com/)
- [`sqlalchemy`](https://www.sqlalchemy.org/)
- [`pydantic[email]`](https://docs.pydantic.dev/)
- [`ruff`](https://docs.astral.sh/ruff/) (linter/formatter)
- [`pytest`](https://docs.pytest.org/), [`pytest-cov`](https://pytest-cov.readthedocs.io/)
- [`mkdocs`](https://www.mkdocs.org/)
- [`taskipy`](https://github.com/illBeRoy/taskipy)

---

## Tasks automatizadas taskipy

Automatize os comandos mais comuns do projeto utilizando [taskipy](https://github.com/illBeRoy/taskipy):

| Tarefa        | Comando            | Descricao                                 |
|---------------|--------------------|-------------------------------------------|
| **run**       | `task run`         | Executa a aplicacao FastAPI               |
| **lint**      | `task lint`        | Lint com Ruff                             |
| **format**    | `task format`      | Formata o codigo com Ruff                 |
| **test**      | `task test`        | Executa os testes + coverage              |
| **pre_test**  | `task pre_test`    | Lint antes dos testes                     |
| **post_test** | `task post_test`   | Gera relatorio HTML do coverage           |

Veja todas as tasks em [`pyproject.toml`](pyproject.toml).

---

## Como rodar o projeto

1. Instale as dependencias ([veja Setup rapido](#setup-rapido))
2. Ative o ambiente virtual:

```bash
poetry shell
```

3. Execute a aplicacao:

```bash
task run
```

Acesse em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)

---

## Testes

Execute todos os testes com cobertura:

```bash
task test
```

O relatorio HTML estara em `htmlcov/`.

---

## Documentacao

Este projeto utiliza **MkDocs** para documentacao estatica.

- Para rodar localmente:

```bash
poetry run mkdocs serve
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Boas praticas adotadas

- **Gerenciamento de dependencias com Poetry**
- **Ambiente reproduzivel e versionado** (`pyenv`, `.python-version`, `poetry.lock`)
- **Separacao clara entre codigo-fonte e testes**
- **Lint/Format automaticos**
- **Tasks automatizadas com Taskipy**
- **Cobertura total de testes**
- **Configuracao pronta para CI/CD**
- **Documentacao pronta para crescer**
- **Estrutura escalavel e reutilizavel**

---

## Dicas interativas e links uteis

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Poetry Docs](https://python-poetry.org/docs/)
- [Ruff Docs](https://docs.astral.sh/ruff/)
- [MkDocs Docs](https://www.mkdocs.org/)

<div align="center">

Dica:  
Use o comando abaixo para adicionar um pacote facilmente:

```bash
poetry add <nome-do-pacote>
```
</div>

---

## Autor

- [LoboProgrammingg](mailto:matheusloboo2001@gmail.com)

---

## Licenca

Este projeto esta sob a licenca MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

Sinta-se a vontade para usar, contribuir e sugerir melhorias! Este repositorio e atualizado constantemente para refletir as melhores praticas em projetos FastAPI modernos.

</div>