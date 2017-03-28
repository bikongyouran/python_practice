# -*- coding:utf-8 -*-


import urllib, urllib2, sys
import ssl
import json
import base64

# img_path = 'C:\Users\junjlin\Desktop\sample_doc_us.jpg'
# img_base64=''
# with open(img_path, 'rb') as infile:
#     s = infile.read()
#     img_base64 = base64.b64encode(s)
#
#
#
# host = 'https://dm-51.data.aliyun.com'
# path = '/rest/160601/ocr/ocr_idcard.json'
# method = 'POST'
# appcode = 'd3870ec56f9c497aa0ad57dd7c94c5a4'
# querys = ''
# # bodys = {}
# url = host + path
# data = "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"
#
#
# # bodys = {"inputs":[{"image":{"dataType":50,"dataValue":data},"configure":{"dataType":50,"dataValue":\"{\\"side\\":\\\"face\\\"}\"}}]}
# bodys = {"inputs": [
#     {
#         "image": {
#             "dataType": 50,
#             "dataValue": img_base64
#         },
#         "configure": {
#             "dataType": 50,
#             "dataValue": '{\"side\":\"face\"}'
#         }
#     }
# ]
# }
#
# post_data = bodys
# request = urllib2.Request(url)
# request.add_header('Authorization', 'APPCODE 3F2504E04F8911D39A0C0305E82C3301')
# # request.add_header('Content-Type', 'application/json; charset=UTF-8')
# request.add_header('Content-Type', 'application/json')
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# # response = urllib2.urlopen(request, json.dumps(post_data),context=ctx)
# response = urllib2.urlopen(request, json.dumps(post_data),context=ctx)
# print response.status_code
# content = response.read()
# if (content):
#     print(content)

# headers = {'Authorization':'APPCODE 3F2504E04F8911D39A0C0305E82C3301','Content-Type':'application/json'}
# r = requests.post(url, data=json.dumps(post_data), cert=ssl.CERT_NONE, headers=headers)
# print r.status_code
# if r.status_code == 200:
#     print r.text


if __name__ == "__main__":
    img_path = 'C:\Users\junjlin\Desktop\sample_doc_us.jpg'
    img_base64 = ''
    with open(img_path, 'rb') as infile:
        s = infile.read()
        img_base64 = base64.b64encode(s)
        print img_base64