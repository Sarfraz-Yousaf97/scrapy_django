# -*- coding: utf-8 -*-
import scrapy


class FreePatentSpider(scrapy.Spider):
    name = 'freepatent'
    allowed_domains = ['freepatentsonline.com']
    search_value = 'iphone'
    start_urls = [f'https://www.freepatentsonline.com/result.html?sort=relevance&srch=top&query_txt={search_value}&submit=&patents_us=on']
     
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'

    def parse(self, response):
        for data in response.xpath("//table[@class='listing_table']//td//a"):
            text = data.xpath(".//text()").get()
            related_link = data.xpath(".//@href").get()
            absolute_url = f"https://www.freepatentsonline.com{related_link}"
            yield{
                'text':text, 
                'related_link':absolute_url,
                # 'absolute_url':absolute_url
        }