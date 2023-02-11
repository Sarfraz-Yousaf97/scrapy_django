# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from main.models import Quote, FreePatent, LogoModel,TrademarkModel,ImageModel
from .spiders.googlepatent import model
from .enums import ModelChoices
class ScrapyAppPipeline(object):
    # def process_item(self, item, spider):
    #     quote = Quote(text=item.get('text'), related_link=item.get('related_link'))
    #     quote.save()
    #     return item
    
    def process_item(self, item, spider):
        # if model == ModelChoices.TRADEMARK.value:
        #     quote = TrademarkModel(title=item.get('title'), description=item.get('description'))
        #     quote.save()
        #     return item
        # if model == ModelChoices.PATENT.value:
        #     quote = FreePatent(title=item.get('title'), description=item.get('description'))
        #     quote.save()
        #     return item
        # if model == ModelChoices.LOGO.value:
        #     quote = LogoModel(title=item.get('title'), description=item.get('description'))
        #     quote.save()
        #     return item
        # if model == ModelChoices.IMAGE.value:
        #     quote = ImageModel(title=item.get('title'), description=item.get('description'))
        #     quote.save()
        #     return item
        return item
    # pass
