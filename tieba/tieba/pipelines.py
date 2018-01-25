# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
pipelines.py主要作用为爬虫数据的处理，即用于爬虫数据的清洗和入库操作。
'''
import pymongo
class TiebaPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        test = client['test']
        tieba = test['tieba']
        self.post = tieba
    def process_item(self , item , spider):
        info = dict(item)
        self.post.insert(info)
        return item