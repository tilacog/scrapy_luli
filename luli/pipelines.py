# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

def clean_list(lst):
    cl = ''.join([i.replace('\n','').strip() for i in lst])
    return cl

class LuliPipeline(object):
    def process_item(self, item, spider):
        """
        Discards empty items
        """
        if not item['title']:
            raise DropItem('Invalid item, MOAMAMAMOAMAOMOAOMAMA')
        
        # Clean fields
        for key in ['title', 'date', 'content']:
            item[key] = clean_list(item[key]) 
        
        return item


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        uid = (item['url'], item['spider'])
        if uid in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(uid)
            return item
