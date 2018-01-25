# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from tieba.items import TiebaItem  #导入库和类
from scrapy.http import Request

class tieba(CrawlSpider):  #定义爬虫类
    name = "tieba"         #爬虫名
    start_urls = ['https://www.zhihu.com/topic/19552832/top-answers?page=1'] #开始URL

    def parse(self , response):      #定义parse()函数
        item = TiebaItem()          #实例化类
        selector =Selector(response)

        infos=selector.xpath('//*[@id="TopicMain"]/div[2]/div/div')
        print(infos)
        for info in infos:
            try:
                question = info.xpath('div/div/h2/div/a/text()').extract()[0].strip()
                # favour = info.xpath('div/div/div[1]/div[1]/a/text()').extract()[0]
                # user = info.xpath('div/div/div[1]/div[3]/span/span[1]/a/text()').extract()[0]
                # user_info = info.xpath('div/div/div[1]/div[3]/span/span[2]/text()').extract()[0].strip()
                # content = info.xpath('div/div/div[1]/div[5]/div/text()').extract()[0].strip()
                item['question'] = question
                # item['favour'] = favour
                # item['user'] = user
                # item['content']= content
                yield item     #返回爬虫数据
            except IndexError:
                pass    #pass 掉 IndexError错误
        urls = ['https://www.zhihu.com/topic/19552832/top-answers?page={}'.format(str(i)) for i in range(2,50)]
        for url in  urls:
            yield Request(url,callback=self.parse)    #回调函数
