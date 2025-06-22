# 🚀 learning-fastapi

[![Python Version](https://img.shields.io/badge/python-3.11.9-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3119/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.12-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Poetry](https://img.shields.io/badge/Poetry-1.8.2-60A5FA?logo=python)](https://python-poetry.org/)
[![License](https://img.shields.io/github/license/LoboProgrammingg/FastAPI?color=brightgreen)](LICENSE)
[![Build status](https://img.shields.io/badge/test-passing-brightgreen?logo=pytest&logoColor=white)](#testes)
[![Coverage Status](https://img.shields.io/badge/coverage-100%25-brightgreen)](#testes)
[![Code Style](https://img.shields.io/badge/code%20style-ruff-0B3D91?logo=python)](https://docs.astral.sh/ruff/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](#status-do-projeto)

---

## ⚠️ Status do Projeto

> **Este projeto está em desenvolvimento e poderá receber atualizações frequentes, melhorias e ajustes. Fique atento a novas versões!**

---

## ✨ Sobre o Projeto

Este repositório foi criado para servir como **base de referência** para novos projetos FastAPI, trazendo as melhores práticas de organização, gerenciamento de dependências, tasks automatizadas, qualidade de código e documentação.

- **Python:** Gerenciado via pyenv (versão 3.11.9)
- **Gerenciador de dependências:** Poetry
- **Framework web:** FastAPI
- **ORM:** SQLAlchemy
- **Validação:** Pydantic
- **Tasks:** Taskipy
- **Linter & Formatter:** Ruff
- **Testes:** Pytest + Coverage
- **Documentação:** MkDocs

---

## 📋 Índice

- [Setup Rápido](#-setup-rápido)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Dependências](#-dependências-principais)
- [Tasks Automatizadas](#-tasks-automatizadas-taskipy)
- [Como rodar](#-como-rodar-o-projeto)
- [Testes](#-testes)
- [Documentação](#-documentação)
- [Boas Práticas](#-boas-práticas-adotadas)
- [Autor](#-autor)
- [Licença](#-licença)

---

## 🛠️ Setup Rápido

<details>
<summary><strong>Mostrar instruções detalhadas</strong></summary>

### 1. Dependências do Sistema

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

#### Configure o shell:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
exec "$SHELL"
```
> Para Zsh, altere `~/.bashrc` para `~/.zshrc`.

### 3. Instale e defina o Python

```bash
pyenv install 3.11.9
pyenv global 3.11.9
python --version # Deve retornar Python 3.11.9
```

### 4. Instale o pipx e o Poetry

```bash
sudo apt install pipx
pipx install poetry
pipx ensurepath
```
> Reinicie o terminal se necessário.

### 5. Configure o projeto

```bash
pyenv local 3.11.9
poetry install
```
</details>

---

## 🏗️ Estrutura do Projeto

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
│   ├── __init.py__
│   ├── test_db.py
│   └── test_app.py
│   └── conftest.py
├── .python-version
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── poetry.lock
├── .python-version
├── mkdocs.yml
├── README.md
└── ...
```

- **src/**: Código fonte do app
- **tests/**: Testes automatizados
- **pyproject.toml**: Configuração do projeto e dependências

---

## 📦 Dependências Principais

- `fastapi[standard]`
- `sqlalchemy`
- `pydantic[email]`

### Dev e Ferramentas

- `ruff` (lint e format)
- `pytest`, `pytest-cov`
- `mkdocs`
- `taskipy`

---

## ⚡ Tasks Automatizadas (Taskipy)

O projeto utiliza [taskipy](https://github.com/illBeRoy/taskipy) para facilitar comandos recorrentes:

| Tarefa        | Comando                       | Descrição                                |
|---------------|------------------------------|------------------------------------------|
| run           | `task run`                   | Executa a aplicação FastAPI              |
| lint          | `task lint`                  | Lint com Ruff                            |
| format        | `task format`                | Formata o código com Ruff                |
| test          | `task test`                  | Executa os testes + coverage             |
| pre_test      | `task pre_test`              | Lint antes dos testes                    |
| post_test     | `task post_test`             | Gera relatório HTML do coverage          |

Veja todas as tasks em [pyproject.toml](pyproject.toml).

---

## 🧑‍💻 Como rodar o projeto?

1. Instale as dependências (veja [Setup Rápido](#-setup-rápido))
2. Ative o ambiente:

```bash
poetry shell
```

3. Execute a aplicação:

```bash
task run
```

Acesse em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)

---

## 🧪 Testes

Execute todos os testes com coverage:

```bash
task test
```

Relatório HTML será gerado em `htmlcov/`.

---

## 📝 Documentação

Este projeto utiliza **MkDocs** para documentação estática.

- Para rodar localmente:

```bash
poetry run mkdocs serve
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🏅 Boas Práticas Adotadas

- **Gerenciamento de dependências com Poetry**
- **Ambiente reprodutível e versionado (pyenv, .python-version, poetry.lock)**
- **Separação clara entre código fonte e testes**
- **Linting & Formatting automáticos**
- **Tasks automatizadas**
- **Configuração completa para CI/CD**
- **Documentação pronta para crescer**
- **Estrutura escalável e reutilizável**

---

## 🎯 Dicas Interativas & Links Úteis

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Poetry Docs](https://python-poetry.org/docs/)
- [Ruff Docs](https://docs.astral.sh/ruff/)
- [MkDocs Docs](https://www.mkdocs.org/)

<div align="center">

💡 **Dica:**  
Use o comando abaixo para adicionar um pacote facilmente:

```bash
poetry add <nome-do-pacote>
```
</div>

---

## 👤 Autor

- [LoboProgrammingg](mailto:matheusloboo2001@gmail.com)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> **Este repositório está em desenvolvimento e poderá ser atualizado com frequência para refletir as melhores práticas em projetos FastAPI modernos. Sinta-se à vontade para utilizar, contribuir e sugerir melhorias!**