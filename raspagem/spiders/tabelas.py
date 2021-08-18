import scrapy


class TabelasSpider(scrapy.Spider):
    name = "tabelas"

    def start_requests(self):
        urls = [
            f"http://www.governotransparente.com.br/transparencia/projetos/resultado/44669490?inicio=01%2F01%2F2011&fim=17%2F08%2F2021&codobra=&nmobra=&datainfo=MTIwMjEwODE4MTQ0N1BQUA%3D%3D&clean=false",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tabela = response.css("#datatable-buttons")

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

            linhas_formatadas.append(
                {
                    "codigo": linha_formatada[0],
                    "nome": linha_formatada[1],
                    "inicio": linha_formatada[2],
                    "fim": linha_formatada[3],
                    "prazo_em_dias": linha_formatada[4],
                    "crea_da_obra": linha_formatada[5],
                    "valor": linha_formatada[6],
                    "liquido": linha_formatada[7],
                    "pagamento": linha_formatada[8],
                    "percentual": linha_formatada[9],
                }
            )

        return linhas_formatadas
