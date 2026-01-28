from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Atividade
from datetime import datetime
from controllers.usuarios import login_obrigatorio

# blueprint das rotas de atividades
atividades_bp = Blueprint('atividades', __name__)

@atividades_bp.route('/', methods=['GET'])
@login_obrigatorio
def listar():
    # lista atividades ordenadas pela data de criação
    atividades = Atividade.query.order_by(Atividade.data_criacao.desc()).all()
    return render_template('atividades/lista.html', atividades=atividades)

@atividades_bp.route('/novo', methods=['GET', 'POST'])
@login_obrigatorio
def novo():
    if request.method == 'POST':
        # coleta dados do formulário
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        data_entrega_str = request.form.get('data_entrega')
        disciplina = request.form.get('disciplina')
        tipo = request.form.get('tipo')   

        # valida campos obrigatórios
        if not titulo or not data_entrega_str:
            flash('Título e Data de entrega são obrigatórios!', 'danger')
            return redirect(url_for('atividades.novo'))

        # valida formato de data
        try:
            data_entrega = datetime.strptime(data_entrega_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de data inválido!', 'danger')
            return redirect(url_for('atividades.novo'))
        
        # cria nova atividade
        nova_atividade = Atividade(
            titulo=titulo,
            descricao=descricao,
            data_entrega=data_entrega,
            disciplina=disciplina,
            tipo=tipo  
        )
        
        db.session.add(nova_atividade)
        db.session.commit()
        
        flash('Atividade cadastrada com sucesso!', 'success')
        return redirect(url_for('atividades.listar'))
    
    return render_template('atividades/form.html')

@atividades_bp.route('/deletar/<int:id>', methods=['POST'])
@login_obrigatorio
def deletar(id):
    # busca atividade pelo id
    atividade = Atividade.query.get_or_404(id)
    
    db.session.delete(atividade)
    db.session.commit()

    flash('Atividade removida com sucesso!', 'warning')
    return redirect(url_for('atividades.listar'))

@atividades_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_obrigatorio
def editar(id):
    # busca atividade pelo id
    atividade = Atividade.query.get_or_404(id)

    if request.method == 'POST':
        # atualiza campos
        atividade.titulo = request.form.get('titulo')
        atividade.descricao = request.form.get('descricao')
        data_entrega_str = request.form.get('data_entrega')
        atividade.disciplina = request.form.get('disciplina')
        atividade.tipo = request.form.get('tipo')   

        # valida data
        try:
            atividade.data_entrega = datetime.strptime(data_entrega_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Formato de data inválido!', 'danger')
            return redirect(url_for('atividades.editar', id=id))

        db.session.commit()
        flash('Atividade atualizada com sucesso!', 'success')
        return redirect(url_for('atividades.listar'))

    return render_template('atividades/form.html', atividade=atividade)
