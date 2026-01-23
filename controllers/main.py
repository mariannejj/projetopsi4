from flask import Blueprint, render_template, session
from models import Atividade
from datetime import date

# blueprint principal do sistema
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # página inicial
    return render_template('index.html')

@main_bp.route('/dashboard')
def dashboard():
    # total de atividades cadastradas
    total_atividades = Atividade.query.count()

    # atividades com entrega hoje
    hoje = date.today()
    atividades_hoje = Atividade.query.filter_by(data_entrega=hoje).count()

    # renderiza o dashboard com os dados
    return render_template(
        'dashboard.html',
        total_atividades=total_atividades,
        atividades_hoje=atividades_hoje
    )
