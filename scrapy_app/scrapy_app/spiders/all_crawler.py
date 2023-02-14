import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from amazone import AmazoneSpider
from googlepatent import FreePatentSpider



settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(FreePatentSpider)
process.crawl(AmazoneSpider)
process.start()