import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from amazone import AmazoneSpider
# from freepatent import FreePatentSpider


# import os
# import sys
# import django

# sys.path.append(os.path.dirname(os.path.abspath('../')))
# os.environ["DJANGO_SETTINGS_MODULE"] = "track_patent.settings"
# django.setup()

class MySpider1(scrapy.Spider):

    name = 'amazone'
    allowed_domains = ['www.amazon.com']
    search_value = 'phone'
    start_urls = [f'https://www.amazon.com/s?k={search_value}&crid=3LQ30S4EVLU6C&sprefix={search_value}%2Caps%2C480&ref=nb_sb_noss_1']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    def request_header(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, headers={'User-Agent':self.user_agent})

    def parse(self, response):
        text = response.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/span/text()").get()
        url_link = response.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/a/@href").get()
        absolute_url = f"https://www.amazon.com/{url_link}"
        imageamazone = response.xpath("//img[@class='s-image']/@src").get() 
        # yield response.follow(url = absolute_url, callback = self.other_link, meta={'title':text, 'imageamazone':imageamazone})
        yield{
            'text':text,
            'url':absolute_url,
            'image':imageamazone
        }
    

class MySpider2(scrapy.Spider):
    name = 'hsn'
    allowed_domains = ['www.hsn.com']
    start_urls = ['https://www.hsn.com/shop/laptops/ec0033?rid=2124&query=laptop&isSuggested=false']

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    def request_header(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, headers={'User-Agent':self.user_agent})
    
    def parse(self, response):
        title = response.xpath("//div[@class='info']/div/a/span/span/text()").get()
        related_link = response.xpath("//div[@class='info']/div/a/@href").get()
        absolute_url = f"https://www.hsn.com/{related_link}"
        image = response.xpath("(//div[@class='swatches']/a)[1]/img/@src").get()
        image1 = response.xpath("(//div[@class='swatches']/a)[2]/img/@src").get()
        # yield{
        #     'title':title,
        #     'related_link':related_link,
        #     'absolute_url':absolute_url,
        #     'image':image,
        #     'image1':image1
        # }

        yield response.follow(url = absolute_url, callback = self.other_link, meta={'image':image,'image1':image1})
    

    def other_link(self, response):
        image = response.request.meta['image']
        image1 = response.request.meta['image1']
        title = response.xpath("//span[@id='product-name']/text()").get()


        yield{
            'image': image,
            'image1': image1,
            'title': title,
        }

settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start()