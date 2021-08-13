import pymongo
class ConexaoDB:
    def __init__(self) -> None:
        try:
            mongo = pymongo.MongoClient(
                host="localhost", port=27017, serverSelectionTimeoutMS=1000
            )
            self.db = mongo.nossa_construcao
            mongo.server_info()

        except Exception as error:
            print("Error - ", error)
