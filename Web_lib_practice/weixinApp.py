#coding: utf-8
import requests
from bs4 import BeautifulSoup
# write Chinese character to file.
import codecs
import json

# f = 'test.txt'
# i = 0


# def write_file(url):
#     responseText = requests.get(url).text
#     soup = BeautifulSoup(responseText,'html.parser')
#     with codecs.open(f, 'a', 'utf-8') as file:
#         for txt in soup.find_all(class_='text'):
#             contentList = txt.find_all('p')
#             content = ''
#             for con in contentList:
#                 content = content + con.get_text() + '\t'
#             file.write(content + '\n')
#             file.write('\n')

if __name__ == '__main__':
    ### send to weixin
    url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=&corpsecret='
    rep = requests.get(url)
    jsonData = json.loads(rep.text) #make the response as a dict object
    token = jsonData['access_token']
    url_send_mes = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token
    print 'url_send_mes:' + url_send_mes

    ### grab jokes
    responseText = requests.get('http://jandan.net/duan').text
    soup = BeautifulSoup(responseText,'html.parser')
    txt = soup.find_all(class_='text')
    content = txt.find('p').get_text()
    mes_data = {"touser": "@all","msgtype": "text","agentid": 1,"text": {"content": content},"safe":"0"}
    r = requests.post(url_send_mes,data=json.dumps(mes_data))
    print r
    print r.text

    # for txt in soup.find_all(class_='text'):
    #     contentList = txt.find_all('p')
    #     content = ''
    #     for con in contentList:
    #         content = content + con.get_text() + '\t'
    #         print "temp content : " + content
    #     mes_data = {"touser": "@all","msgtype": "text","agentid": 1,"text": {"content": content},"safe":"0"}
    #     try:
    #         r = requests.post(url_send_mes,data=json.dumps(mes_data))
    #         print r
    #         print r.text
    #     except Exception as ex:
    #         print "error happens!" + ex.message






    # previousPage = 'http://jandan.net/duan'
    # while i < 2:
    #     write_file(previousPage)
    #     previousPage = BeautifulSoup(requests.get(previousPage).text,'html.parser').find(class_='previous-comment-page').get('href')
    #     i += 1


