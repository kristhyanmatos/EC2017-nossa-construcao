# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class NossaContrucaoPipeline:
    def __init__(self) -> None:
        self.conexao = pymongo.MongoClient(
            "localhost", 27017,
        )
        banco = self.conexao["nossa_construcao"]
        self.colecao = banco["tabelas"]

    def process_item(self, item, spider):
        self.colecao.insert(dict(item))
        return item
