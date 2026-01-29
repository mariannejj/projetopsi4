from flask import Flask
from flask_cors import CORS
from db import init_db
import items

app = Flask(__name__, instance_relative_config=True)
app.config["database"] = "plataforma_estudos.db"

CORS(app)

with app.app_context():
    init_db()

app.route("/items", methods=["GET"])(items.listar)
app.route("/items", methods=["POST"])(items.criar)
app.route("/items/<int:id>", methods=["PUT"])(items.editar)
app.route("/items/<int:id>/status", methods=["PATCH"])(items.mudar_status)
app.route("/items/<int:id>", methods=["DELETE"])(items.remover)

app.run(debug=True)
