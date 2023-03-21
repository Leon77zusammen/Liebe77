# -*- coding: utf-8 -*-
import http.client, urllib, json
conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'a3eb7772fb38282051dac995cb8011d7'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/lzmy/index',params,headers)
tianapi = conn.getresponse()
result = tianapi.read()
data = result.decode('utf-8')
dict_data = json.loads(data)
print(dict_data)
print(dict_data["result"]["saying"])