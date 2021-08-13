import json
from flask import Flask, Response
from conexao import ConexaoDB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conexao = ConexaoDB()
db = conexao.db


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


if __name__ == "__main__":
    app.run(port=80, debug=True)
