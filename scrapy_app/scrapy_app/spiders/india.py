import scrapy

    

class IndiaSpider(scrapy.Spider):
    name = 'indiamart'
    allowed_domains = ['indiamart.com']
    search_value = 'car'
    start_urls = [f'https://dir.indiamart.com/search.mp?ss=laptop&prdsrc=1&res=RC4&res=RC3']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    def request_header(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, headers={'User-Agent':self.user_agent})

    def parse(self, response):
        title = response.xpath("//span[2]/text()").get()

        yield{
            'title':title
        }