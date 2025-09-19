# Mercado - PSI

Um marketplace simples feito em Flask para venda de livros, cursos e equipamentos de programação e hardware (processadores, placas, etc).

## Tecnologias usadas

* Python 3.17
* Flask
* SQLAlchemy (ORM)
* MySQL (Banco de dados)
* Bootstrap 

## Funcionalidades

* CRUD completo (Criar, Ler, Atualizar, Deletar) para produtos: livros, cursos e equipamentos.
* Interface simples para gerenciamento dos produtos.
* Persistência dos dados com MySQL e SQLAlchemy.

---

## Como clonar e rodar localmente

### Pré-requisitos

* Python 3 instalado
* MySQL instalado e configurado
* Git instalado

### Passos

1. Clone o repositório:

```bash
git clone https://github.com/flaubersauan/MercadoPSI.git
cd mercadoPSI
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados MySQL:

* Crie uma database chamado `mercadoPSI` (ou o nome que preferir):

```sql
CREATE DATABASE mercadopsi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

* Atualize a string de conexão no arquivo de configuração do Flask:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost/mercadoPSI'
```

5. Inicialize o banco de dados (criação direta das tabelas):

```python
from app import db
db.create_all()
```

6. Rode a aplicação:

```bash
flask run
```

7. Acesse no navegador:

```
http://localhost:5000
```

---

## Estrutura do projeto

Alteravel

```
mercadoPSI/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   └── static/
├── config.py
├── requirements.txt
└── run.py
```

---

## Como contribuir

1. Fork o projeto
2. Crie sua branch: `git checkout -b minha-feature`
3. Commit suas alterações: `git commit -m 'Adicionei nova feature'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## Contato

Equipe Mercado PSI - [emailresponsavel@gmail.com](mailto:paulofernandesalves30@gmail.com)

---

