from flask import request, jsonify
from settings import tipos_permitidos, status_permitidos
from db import get_db

def validar(dados, parcial=False):
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
    conn.close()
    return jsonify({"ok": True}), 201

def editar(id):
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
    return jsonify({"ok": True})

def mudar_status(id):
    dados = request.get_json()
    if dados.get("status") not in status_permitidos:
        return jsonify({"error": "status invalido"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("update items set status = ? where id = ?", (dados["status"], id))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})

def remover(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("delete from items where id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"ok": True})
