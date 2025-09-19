from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy

class User(db.Model , UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    email = db.Column(db.String(180) , unique = True , nullable = False)
    password = db.Column(db.String(180) , nullable = False)

    produtos_vendidos = db.relationship('ProdutoVendido', backref='vendedor', lazy=True)

class Produtos(db.Model):
    __tablename__ = 'tb_Produtos'

    id_produto = db.Column(db.Integer , primary_key = True , autoincrement = True)
    nome_produto = db.Column(db.Striger(180) , nullable = False)
    preco_produto = db.Column(db.Numeric(10,2) , nullable = False)

class Produtos_Vendidos(db.Model):
    __tablename__ = 'produtos_vendidos'

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    data_venda = db.Column(db.DateTime, nullable=False)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

