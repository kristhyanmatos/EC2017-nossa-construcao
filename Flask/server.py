from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host = "localhost",
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.tabela
    mongo.server_info()

except :
    print("Error - cannot connect to db")
#####################################################
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(response = json.dumps(data),
        status=200,
        mimetype="application/json"
        )

    except:
        print(ex)
        return Response(response = json.dumps({"message":"deu ruim"}), status=500, mimetype="application/json")


############################
if __name__ == "__main__":
    app.run(port=80, debug=True)