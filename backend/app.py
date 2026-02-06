from pathlib import Path
from flask import Flask, send_from_directory
from flask_cors import CORS
from db import init_db
import items

def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config["database"] = "agenda.db"

    CORS(app)

    with app.app_context():
        init_db()

    web_dir = Path(__file__).resolve().parent.parent / "web"

    @app.get("/")
    def home():
        return send_from_directory(web_dir, "index.html")

    @app.get("/<path:filename>")
    def web_files(filename):
        return send_from_directory(web_dir, filename)

    app.route("/items", methods=["GET"])(items.listar)
    app.route("/items", methods=["POST"])(items.criar)
    app.route("/items/<int:id>", methods=["PUT"])(items.editar)
    app.route("/items/<int:id>/status", methods=["PATCH"])(items.mudar_status)
    app.route("/items/<int:id>", methods=["DELETE"])(items.remover)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
