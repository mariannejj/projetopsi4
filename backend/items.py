from flask import request, jsonify
from settings import tipos_permitidos, status_permitidos
from db import get_db
from datetime import datetime


def validar(dados, parcial=False):

    if not dados:
        return "dados invalidos"
    if not parcial:
        if "titulo" not in dados or len(dados["titulo"].strip()) < 3:
            return "titulo invalido"
        if dados.get("tipo") not in tipos_permitidos:
            return "tipo invalido"
        if dados.get("status") not in status_permitidos:
            return "status invalido"
    if "valor" in dados and dados["valor"] is not None:
        try:
            if float(dados["valor"]) < 0:
                return "valor invalido"
        except:
            return "valor invalido"
    if "data" in dados and dados["data"] not in (None, ""):
        try:
            datetime.strptime(dados["data"], "%Y-%m-%d")
        except:
            return "data invalida"

    return None



def buscar_item_por_id(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("select * from items where id = ?", (id,))
    item = cur.fetchone()
    conn.close()
    if item:
        return dict(item)
    return None


def listar():
    tipo = request.args.get("tipo")
    status = request.args.get("status")

    sql = "select * from items"
    params = []

    if tipo and status:
        sql += " where tipo = ? and status = ?"
        params = [tipo, status]
    elif tipo:
        sql += " where tipo = ?"
        params = [tipo]
    elif status:
        sql += " where status = ?"
        params = [status]

    conn = get_db()
    cur = conn.cursor()
    cur.execute(sql, params)
    dados = cur.fetchall()
    conn.close()

    return jsonify([dict(d) for d in dados])


def criar():
    dados = request.get_json()
    erro = validar(dados)
    if erro:
        return jsonify({"error": erro}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        insert into items (titulo, tipo, status, data, valor)
        values (?, ?, ?, ?, ?)
    """, (
        dados["titulo"],
        dados["tipo"],
        dados["status"],
        dados.get("data"),
        dados.get("valor")
    ))
    conn.commit()

    novo_id = cur.lastrowid  # pega o id do item crisdo
    conn.close()

    item = buscar_item_por_id(novo_id)
    return jsonify(item), 201


def editar(id):
    #404 se n existir
    if not buscar_item_por_id(id):
        return jsonify({"error": "item nao encontrado"}), 404

    dados = request.get_json()
    erro = validar(dados)
    if erro:
        return jsonify({"error": erro}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        update items
        set titulo = ?, tipo = ?, status = ?, data = ?, valor = ?
        where id = ?
    """, (
        dados["titulo"],
        dados["tipo"],
        dados["status"],
        dados.get("data"),
        dados.get("valor"),
        id
    ))
    conn.commit()
    conn.close()

    item = buscar_item_por_id(id)
    return jsonify(item)


def mudar_status(id):
    #404 se n existir
    if not buscar_item_por_id(id):
        return jsonify({"error": "item nao encontrado"}), 404

    dados = request.get_json()
    if dados.get("status") not in status_permitidos:
        return jsonify({"error": "status invalido"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("update items set status = ? where id = ?", (dados["status"], id))
    conn.commit()
    conn.close()

    item = buscar_item_por_id(id)
    return jsonify(item)


def remover(id):
    # pega o item antes (pra poder retornar ele)
    item = buscar_item_por_id(id)
    if not item:
        return jsonify({"error": "item nao encontrado"}), 404

    conn = get_db()
    cur = conn.cursor()
    cur.execute("delete from items where id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify(item)
