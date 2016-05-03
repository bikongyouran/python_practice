#coding: utf-8
import requests
import json

#企业号开发文档：http://qydev.weixin.qq.com/wiki/index.php?title=%E9%A6%96%E9%A1%B5
# enter 企业号-->设置-->功能设置-->权限管理-->click 系统管理组, and will find CorpID and Secret

url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=&corpsecret='
rep = requests.get(url)
jsonData = json.loads(rep.text) #make the response as a dict object
token = jsonData['access_token']
print token

url_send_mes = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token
print url_send_mes

mes_data = {"touser": "@all","msgtype": "text","agentid": 1,"text": {"content": "this is my first test!!!"},"safe":"0"}
r = requests.post(url_send_mes,data=json.dumps(mes_data))
print r
print r.text
