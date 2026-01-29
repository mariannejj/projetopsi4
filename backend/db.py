import sqlite3
from pathlib import Path
from flask import current_app

def get_db_path() -> str:
    db_file = current_app.config.get("database", "plataforma_estudos.db")
    return str(Path(current_app.instance_path) / db_file)

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db() -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    create table if not exists items (
        id integer primary key autoincrement,
        titulo text not null,
        tipo text not null,
        status text not null,
        descricao text,
        data text,
        valor real
    )
    """)
    conn.commit()
    conn.close()
