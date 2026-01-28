from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Usuario(db.Model):  # tabela usuários
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def set_senha(self, senha):  # criptografa
        self.senha_hash = generate_password_hash(senha)

    def verifica_senha(self, senha):  # verifica
        return check_password_hash(self.senha_hash, senha)

class Atividade(db.Model):  # tabela atividades
    __tablename__ = 'atividade'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    data_entrega = db.Column(db.Date, nullable=False)
    disciplina = db.Column(db.String(50))
    tipo = db.Column(db.String(20), nullable=False, default="Atividade")
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.titulo
