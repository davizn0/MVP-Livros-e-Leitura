# MVP Livros e Leitura

## Sobre o projeto

O MVP Livros e Leitura é uma aplicação web desenvolvida para auxiliar a Biblioteca Social Riacho Fundo II na organização de itens solicitados e doações recebidas.

O sistema permite cadastrar itens em falta, registrar doações e acompanhar as quantidades recebidas.

## Tecnologias utilizadas

- Python

- Flask

- SQLite

- HTML

- CSS

## Funcionalidades

### Login

Acesso à área de gerenciamento por meio de autenticação.

### Cadastro de itens

Cadastro de itens em falta, com nome, categoria e quantidade desejada.

### Registro de doações

Registro das quantidades recebidas para cada item cadastrado.

### Listagem de itens

Visualização dos itens solicitados e acompanhamento das quantidades atendidas.

### Interface

Páginas HTML estilizadas com CSS.

## Estrutura do projeto

```text
livros-leitura/
├── static/
│   └── style.css
├── templates/
│   ├── base.html
│   ├── cadastro.html
│   ├── listagem.html
│   └── login.html
├── tests/
├── app.py
├── livros.db
└── README.md
```

## Como executar o projeto

### Pré requisitos

Python instalado na máquina.

### Clonar o repositório

```bash
git clone https://github.com/davizn0/MVP-Livros-e-Leitura.git
cd MVP-Livros-e-Leitura
```

### Criar o ambiente virtual

```bash
python -m venv .venv
```

### Ativar o ambiente virtual

No Windows:

```powershell
.venv\Scripts\activate
```

### Instalar as dependências

```bash
pip install flask
```

### Executar a aplicação

```bash
python app.py
```

Acesse a aplicação pelo endereço:

http://127.0.0.1:5000

## Testes

O projeto possui uma pasta destinada aos testes. As verificações automatizadas podem ser executadas conforme a configuração do projeto.

## Integração contínua

O projeto utiliza um fluxo de CI no GitHub Actions para executar verificações automaticamente nos Pull Requests.

## Status do projeto

Em desenvolvimento.
