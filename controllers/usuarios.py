from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Usuario
from functools import wraps
from flask import session, redirect, url_for, flash

# blueprint de usuários
usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        # pega dados do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        # verifica se o e-mail já existe
        if Usuario.query.filter_by(email=email).first():
            flash("E-mail já cadastrado!", "danger")
            return redirect(url_for('usuarios.registrar'))

        # cria novo usuário
        novo = Usuario(nome=nome, email=email)
        novo.set_senha(senha)

        db.session.add(novo)
        db.session.commit()

        flash("Usuário registrado com sucesso!", "success")
        return redirect(url_for('usuarios.login'))

    return render_template('usuarios/registrar.html')


@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # coleta dados do login
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = Usuario.query.filter_by(email=email).first()

        # credenciais
        if not user or not user.verifica_senha(senha):
            flash("E-mail ou senha incorretos!", "danger")
            return redirect(url_for('usuarios.login'))

        # salva dados do usuário 
        session['usuario_id'] = user.id
        session['usuario_nome'] = user.nome

        flash("Login realizado!", "success")
        return redirect(url_for('main.index'))

    return render_template('usuarios/login.html')

@usuarios_bp.route('/logout')
def logout():
    # remove usuário 
    session.pop("usuario_id", None)
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("usuarios.login"))


def login_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Você precisa estar logado para acessar esta página!", "danger")
            return redirect(url_for("usuarios.login"))
        return f(*args, **kwargs)
    return decorated
