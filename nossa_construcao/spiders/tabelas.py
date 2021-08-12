import scrapy


class TabelasSpider(scrapy.Spider):
    name = "tabelas"

    def start_requests(self):
        urls = [
            f"http://www.governotransparente.com.br/transparencia/projetos/resultado/44669490?inicio=19%2F12%2F2019&fim=11%2F08%2F2021&codobra=&nmobra=&datainfo=MTIwMjEwODEyMTEwOVBQUA%3D%3D&clean=false",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tabela = response.css("#datatable-buttons")

        # buscar cabeçalho da tabela
        colunas = tabela.xpath("./thead/tr/th")
        colunas_formatadas = []
        for coluna in colunas:
            texto = coluna.xpath("./text()").get()
            colunas_formatadas.append(texto)
        # self.log(f"Cabeçalho {colunas_formatadas}")

        # buscar Conteúdo da tabela
        linhas = tabela.xpath("./tbody/tr")
        linhas_formatadas = []

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

            linhas_formatadas.append(
                {
                    colunas_formatadas[0]: linha_formatada[0],
                    colunas_formatadas[1]: linha_formatada[1],
                    colunas_formatadas[2]: linha_formatada[2],
                    colunas_formatadas[3]: linha_formatada[3],
                    colunas_formatadas[4]: linha_formatada[4],
                    colunas_formatadas[5]: linha_formatada[5],
                    colunas_formatadas[6]: linha_formatada[6],
                    colunas_formatadas[7]: linha_formatada[7],
                    colunas_formatadas[8]: linha_formatada[8],
                    colunas_formatadas[9]: linha_formatada[9],
                }
            )

        return linhas_formatadas
