'''
百度地图api调用
'''
'''
import requests 
address = input('输入地点：')
par = {'address':address,'key':'cb649a25d1f81c145ladbeca73623251'} #get 请求参数
url = 'http://restapi.amap.com/v3/geocode/geo'
res = requests.get(url,par)
print(res.text)
'''
# import requests
# import json
# import pprint
# address = input('输入地点：')
# par = {'address':address,'key':'cb649a25d1f81c145ladbeca73623251'} #get 请求参数
# url = 'http://restapi.amap.com/v3/geocode/geo'
# res = requests.get(url,par)
# json_data =json.loads(res.text)
# pprint.pprint(json_data)

import requests
import json

address = input('输入地点：')
par = {'address':address,'key':'cb649a25d1f81c145ladbeca73623251'} #get 请求参数
url = 'http://restapi.amap.com/v3/geocode/geo'
res = requests.get(url,par)
json_data =json.loads(res.text)
geo =json_data['geocode'][0]['location']
longitude =geo.split(',')[0]
latitude =geo.split(',')[1]
print(longitude,latitude) #解析提取json数据