'''
1 导入程序所需的库
2 用于创建MongDB数据库和集合
3 使用Selenium的webdriver实例化一个浏览器对象，并设置Phantomjs窗口最大化
4 定义了获取商品信息函数。请求传入的URL链接，并隐式等待10s。获取page_source,利用
lxml库解析爬取数据，并存储到MongDB数据库中
5 定义获取翻页后URL的函数。传入当前URL，通过使用selenium和PhantomJS，模拟电脑的
翻页操作，获取下一页URL
6 行为主函数入口。使用Seleniumh和PhantomJS，模拟计算机输入文字，并展开搜索功能，获取
男士短袖的URL，调用获取商品信息的函数
'''

from  selenium  import webdriver
from lxml import etree
import time
import pymongo                                    #导入相应的库文件

client = pymongo.MongoClient('localhost',27017)   #连接数据库
mydb =client['mydb']
taobao=mydb['taobao']                             #创建数据库和数据集合
driver = webdriver.PhantomJS()                    #实例化浏览器
driver.maximize_window()                          #窗口最大化

def get_info(url,page):                           #定义获取商品信息的函数
    page =page+1
    driver.get(url)
    driver.implicitly_wait(10)                    #隐式等待10s
    selector = etree.HTML(driver.page_source)     #请求网页源代码

    infos = selector.xpath('//div[@class ="item J_MouserOnverReq  "]')
    #infos = selector.xpath(' *[ @ id = "mainsrp-itemlist"] / div / div / div[1] / div[2]')
    print(infos)
    for info in  infos:
        data = info.xpath('div/div/a')[0]
        goods= data.xpath('string(.)').strip()
        price = info.xpath('div/div/div/strong/text()')[0]
        sell = info.xpath('div/div/div[@class="deal-cnt"]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div[1]/a/span[2]/text()')[0]
        address = info.xpath('div[2]/div[3]/div[2]/text()')[0]

        commodity = {
            'good':goods,
            'price':price,
            'sell':sell,
            'shop':shop,
            'address':address
        }
        taobao.insert_one(commodity)  #插入数据库
        if page <=50:
            NextPage(url,page)  #进入下一页
        else :
            pass

def NextPage(url,page): #定义下一页函数
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]')\
        .click()
    time.sleep(4)
    driver.get(driver.current_url)
    driver.implicitly_wait(10)
    get_info(driver.current_url,page) #用get_info()函数

if __name__ == '__main__': #程序主入口
    page = 1
    url = 'http://www.taobao.com/'
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('男士短袖')#输入商品名
    driver.find_element_by_class_name('btn-search').click()#单机搜索
    get_info(driver.current_url,page)












