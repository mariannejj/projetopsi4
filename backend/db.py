import sqlite3
from flask import current_app
from pathlib import Path

def get_db():
    caminho = Path(current_app.instance_path) / current_app.config["database"]
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists items (
            id integer primary key autoincrement,
            titulo text not null,
            tipo text not null,
            status text not null,
            data text,
            valor real
        )
    """)
    conn.commit()
    conn.close()

