# API de E-commerce

Esta é uma API baseada em Flask para um sistema de e-commerce. Ela fornece endpoints para autenticação de usuários, gerenciamento de produtos e operações no carrinho de compras.

## Funcionalidades

- **Autenticação**: Funcionalidade de login e logout usando `Flask-Login`.
- **Gerenciamento de Produtos**: Adicionar, atualizar, deletar e recuperar detalhes de produtos.
- **Operações no Carrinho**: Adicionar itens ao carrinho, visualizar o conteúdo do carrinho, remover itens e realizar checkout.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/): Framework web minimalista para Python.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): Extensão para integração com bancos de dados usando SQLAlchemy.
- [Flask-Login](https://flask-login.readthedocs.io/): Extensão para gerenciamento de autenticação de usuários.
- [Flask-Cors](https://flask-cors.readthedocs.io/): Extensão para habilitar CORS (Cross-Origin Resource Sharing).
- [Werkzeug](https://werkzeug.palletsprojects.com/): Biblioteca WSGI para manipulação de requisições e respostas HTTP.

## Requisitos

- Python 3.8 ou superior
- SQLite (banco de dados padrão)

## Instalação

1. Clone o repositório:

   ```bash
   git clone <repository-url>
   cd ecommerce-api-py
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicialize o banco de dados:
   ```python
   from application import database
   database.create_all()
   ```

## Executando a Aplicação

1. Inicie o servidor Flask:

   ```bash
   python application.py
   ```

2. Acesse a API em `http://127.0.0.1:5000`.

## Endpoints da API

### Autenticação

- **POST /login**: Realiza login com nome de usuário e senha.
- **POST /logout**: Realiza logout do usuário atual.

### Produtos

- **GET /api/products**: Recupera todos os produtos.
- **GET /api/products/{product_id}**: Recupera os detalhes de um produto específico.
- **POST /api/products/add**: Adiciona um novo produto (requer login).
- **PUT /api/products/update/{product_id}**: Atualiza um produto (requer login).
- **DELETE /api/products/delete/{product_id}**: Deleta um produto (requer login).

### Carrinho

- **POST /api/cart/add/{product_id}**: Adiciona um produto ao carrinho (requer login).
- **DELETE /api/cart/remove/{product_id}**: Remove um produto do carrinho (requer login).
- **GET /api/cart**: Visualiza o conteúdo do carrinho (requer login).
- **POST /api/cart/checkout**: Realiza o checkout e limpa o carrinho (requer login).

## Documentação Swagger

A API está documentada usando Swagger. Consulte o arquivo `swagger-doc.x-yaml` para especificações detalhadas da API.

## Observações

- Certifique-se de inicializar o banco de dados antes de executar a aplicação.
- Use uma ferramenta como Postman ou cURL para testar os endpoints da API.

## Licença

Este projeto está licenciado sob a Licença MIT.
