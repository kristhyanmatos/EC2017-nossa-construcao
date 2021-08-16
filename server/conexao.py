import pymongo
from server.config_env import URL_DB


class ConexaoDB:
    def __init__(self) -> None:
        try:
            mongo = pymongo.MongoClient(URL_DB)
            self.db = mongo.raspagem
            print("Conectado!")

        except Exception as error:
            print("Error - ", error)
