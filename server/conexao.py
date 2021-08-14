import pymongo
from config_env import URL_DB


class ConexaoDB:
    def __init__(self) -> None:
        try:
            mongo = pymongo.MongoClient(URL_DB)
            self.db = mongo.nossa_construcao
            print(mongo.server_info())

        except Exception as error:
            print("Error - ", error)
