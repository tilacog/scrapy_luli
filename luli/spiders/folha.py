# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from luli.items import LuliItem 

class FolhaSpider(scrapy.Spider):
    name = "folha"
    allowed_domains = ["folha.uol.com.br"]
    start_urls = (
        'http://www1.folha.uol.com.br/colunas/luliradfahrer/',

    )

    def parse(self, response):
        for href in response.css("ol.news > li > a::attr('href')").extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_content_page)

        next_page = response.css("li.next > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)

        

    def parse_content_page(self, response):
        il = ItemLoader(item = LuliItem(), response=response)
        
        il.add_css('content', 'div#articleNew > p::text')
        il.add_css('content', 'div[itemprop="articleBody"] > p')
        
        il.add_css('date', 'div#articleDate::text')
        il.add_css('date', 'header > time[datetime]::attr(datetime)')
        
        il.add_css('title', 'div#articleNew > h1::text')
        il.add_css('title', 'h1[itemprop="headline"]::text')
        
        il.add_value('url', response.url)


        item = il.load_item() 
        yield item


