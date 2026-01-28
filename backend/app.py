from flask import Flask
from models import db

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plataforma_estudos.db'  # banco
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # evita avisos
    app.config['SECRET_KEY'] = 'uma_chave_secreta_aqui'  # sessões

    db.init_app(app)  #  DB

    from controllers.main import main_bp
    from controllers.atividades import atividades_bp
    from controllers.usuarios import usuarios_bp

    app.register_blueprint(main_bp)  # rotas
    app.register_blueprint(atividades_bp, url_prefix='/atividades')
    app.register_blueprint(usuarios_bp, url_prefix="/usuarios")

    with app.app_context():
        db.create_all()  # cria tabelas

    return app

if __name__ == '__main__':
    app = create_app()  # inicia app
    app.run(debug=True)
