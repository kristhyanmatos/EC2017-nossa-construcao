import scrapy


class TabelasSpider(scrapy.Spider):
    name = "tabelas"

    def start_requests(self):
        urls = [
            f"http://www.governotransparente.com.br/transparencia/projetos/resultado/44669490?inicio=01%2F01%2F2010&fim=04%2F08%2F2021&codobra=&nmobra=&datainfo=MTIwMjEwODA0MTcxMFBQUA%3D%3D&clean=false",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tabela = response.css("#datatable-buttons")

        # buscar cabeçalho da tabela
        linhas = tabela.xpath("./thead/tr")

        for linha in linhas:
            colunas = linha.xpath("./th")
            linha_formatada = []
            for coluna in colunas:
                texto = coluna.xpath("./text()").get()
                linha_formatada.append(texto)
            self.log(f"Cabeçalho {linha_formatada}")

        # buscar Conteúdo da tabela
        linhas = tabela.xpath("./tbody/tr")

        for linha in linhas:
            colunas = linha.xpath("./td")
            linha_formatada = []
            for coluna in colunas:
                if len(linha_formatada) == 0:
                    texto = coluna.xpath("./a/span/text()").get()
                else:
                    texto = coluna.xpath("./text()").get()
                linha_formatada.append(texto)
            self.log(f"Linha {linha_formatada}")

        self.log(f"Quantidade de linhas: {len(linhas)}")
