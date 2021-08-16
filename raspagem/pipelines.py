# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class NossaContrucaoPipeline:
    def __init__(self) -> None:
        self.conexao = pymongo.MongoClient(
            "localhost",
            27017,
        )
        banco = self.conexao["raspagem"]
        self.colecao = banco["tabelas"]
        self.dados = list(self.colecao.find())

    def process_item(self, item, spider):
        for dado in self.dados:
            if dado["codigo"] == item["codigo"]:
                return item
        print("Construção salva: ", item["codigo"])
        self.colecao.insert(dict(item))
        return item
