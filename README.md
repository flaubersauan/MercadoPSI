### Mercado - PSI

Um marketplace simples feito em Flask para a venda de livros, cursos e equipamentos de programação e hardware (processadores, placas, etc.).

1.  **Descrição:** Um marketplace simples feito em Flask para a venda de livros, cursos e equipamentos de programação e hardware (processadores, placas, etc.).

2.  **Link do projeto em produção:** Não há link de projeto em produção disponível.

3.  **Lista com as funcionalidades:**

      * CRUD completo (Criar, Ler, Atualizar, Deletar) para produtos: livros, cursos e equipamentos.
      * Interface simples para gerenciamento dos produtos.
      * Persistência dos dados com MySQL e SQLAlchemy.

-----

### 🔧 Instalação

  * **Pré-requisitos:**

      * Python 3 instalado
      * MySQL instalado e configurado
      * Git instalado

  * **Passos:**

    I.  Clone o repositório:

    <!-- end list -->

    ```bash
    git clone https://github.com/flaubersauan/MercadoPSI.git
    cd mercadoPSI
    ```

    II.  Crie e ative um ambiente virtual (recomendado):

    <!-- end list -->

    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No Linux/Mac
    source venv/bin/activate
    ```

    III.  Instale as dependências:

    <!-- end list -->

    ```bash
    pip install -r requirements.txt
    ```

    IV.  Configure o banco de dados MySQL:

    <!-- end list -->

      * Crie uma database chamada `mercadopsi` (ou o nome que preferir):

    <!-- end list -->

    ```sql
    CREATE DATABASE mercadopsi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    ```

      * Atualize a string de conexão no arquivo `app.py`:

    <!-- end list -->

    ```python
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mercadopsi'
    ```

    V.  Inicialize o banco de dados (criação direta das tabelas):

    <!-- end list -->

    ```python
    from app import db
    db.create_all()
    ```

    VI.  Rode a aplicação:

    <!-- end list -->

    ```bash
    flask run
    ```

    VII.  Acesse no navegador:

    <!-- end list -->

    ```
    http://localhost:5000
    ```


### 🛠️ Tecnologias & Libs

  * **Tecnologias:**

      * Python 3.17
      * Flask
      * SQLAlchemy (ORM)
      * MySQL (Banco de dados)
      * Bootstrap

  * **Bibliotecas (listadas no `requirements.txt`):**

      * `bcrypt`
      * `blinker`
      * `cffi`
      * `click`
      * `colorama`
      * `cryptography`
      * `flask`
      * `Flask-Bcrypt`
      * `Flask-Login`
      * `flask-sqlalchemy`
      * `greenlet`
      * `importlib-metadata`
      * `itsdangerous`
      * `jinja2`
      * `MarkupSafe`
      * `mysql-connector`
      * `mysqlclient`
      * `pycparser`
      * `pymysql`
      * `python-dotenv`
      * `sqlalchemy`
      * `typing-extensions`
      * `werkzeug`
      * `zipp`

### ✒️ Autor

  * Alan Pereira da Silva
  * Flauber Sauan Candido Alves
  * João Paulo Fernandes Alves
  * José Ezequiel Oliveira Silva
