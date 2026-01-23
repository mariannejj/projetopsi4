import os

# diretório base do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "123456"  # pode trocar depois
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'estudos.db')}"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
