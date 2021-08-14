import json
from flask import Flask, Response
from conexao import ConexaoDB
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    conexao = ConexaoDB()
    db = conexao.db

    @app.route("/", methods=["GET"])
    def index():
        try:

            return Response(
                response=json.dumps({"ola": "haroldo"}),
                status=200,
                mimetype="application/json",
            )

        except Exception as error:
            return Response(
                response=json.dumps({"message": str(error)}),
                status=500,
                mimetype="application/json",
            )

    @app.route("/nossas-construcoes", methods=["GET"])
    def get_nossas_construcoes():
        try:
            data = list(db.tabelas.find())
            for construcao in data:
                construcao["_id"] = str(construcao["_id"])

            return Response(
                response=json.dumps(data), status=200, mimetype="application/json"
            )

        except Exception as error:
            return Response(
                response=json.dumps({"message": str(error)}),
                status=500,
                mimetype="application/json",
            )

    return app
