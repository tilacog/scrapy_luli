# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst


def remove_nl_and_convert_to_str(p_list):
    return "".join([p.replace('\n','') for p in p_list])

class LuliItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    content = scrapy.Field(serializer=remove_nl_and_convert_to_str, output_processor=TakeFirst())
    url = scrapy.Field()
    
