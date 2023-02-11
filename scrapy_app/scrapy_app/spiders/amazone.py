import scrapy


class AmazoneSpider(scrapy.Spider):
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

    # def other_link(self, response):
    #     title = response.request.meta['title']
    #     imageamazone = response.request.meta['imageamazone']
    #     image = response.xpath("//span[@class='a-button-text']/img/@src").get()

    #     yield{
    #         'title':title,
    #         'image': image,
    #         'imageamazone': imageamazone,
    #     }
