# Megusta - Web App para Delivery

O Megusta é um web app projetado para gerenciar um serviço de delivery de alimentos. Este projeto oferece funcionalidades básicas de autenticação, CRUD de produtos e uma interface intuitiva para administradores.

## Funcionalidades

- **Login e Cadastro de Usuários**: Permite que administradores se autentiquem e criem novos usuários.
- **CRUD de Produtos**: Funcionalidades para criar, ler, atualizar e deletar produtos de alimentação.
- **Dashboard**: Interface administrativa para gerenciar produtos.

## Tecnologias

- **Flask**: Microframework para Python usado para desenvolver o backend.
- **SQLAlchemy**: ORM para interagir com o banco de dados SQLite.
- **Flask-Login**: Gerenciamento de sessões e autenticação de usuários.
- **Bootstrap**: Framework CSS para estilização da interface.

## Estrutura do Projeto

- **`app.py`**: Configuração e inicialização do aplicativo Flask.
- **`models.py`**: Definição dos modelos de banco de dados.
- **`routes.py`**: Rotas e lógica do aplicativo.
- **`templates/`**: Diretório contendo os arquivos HTML.
  - **`base.html`**: Template base para as outras páginas HTML.
  - **`login.html`**: Página de login.
  - **`dashboard.html`**: Página do painel de administração.
  - **`create_product.html`**: Página para criar novos produtos.
  - **`home.html`**: Página inicial do site.
- **`static/`**: Diretório para arquivos estáticos como CSS e JS.

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd megusta
