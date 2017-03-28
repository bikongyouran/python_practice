import urllib, urllib2, sys
import ssl


host = 'https://dm-51.data.aliyun.com'
path = '/rest/160601/ocr/ocr_idcard.json'
method = 'POST'
appcode = '你自己的AppCode'
querys = ''
bodys = {}
url = host + path

bodys[''] = "{\"inputs\":[{\"image\":{\"dataType\":50,\"dataValue\":\"base64_image_string(#括号内为描述，不需上传，图片以base64编码的string)\"},\"configure\":{\"dataType\":50,\"dataValue\":\"{\\\"side\\\":\\\"face(#括号内为描述，不需上传，身份证正反面类型:face/back)\\\"}\"}}]}"
post_data = bodys['']
request = urllib2.Request(url, post_data)
request.add_header('Authorization', 'APPCODE ' + appcode)
//根据API的要求，定义相对应的Content-Type
request.add_header('Content-Type', 'application/json; charset=UTF-8')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib2.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)