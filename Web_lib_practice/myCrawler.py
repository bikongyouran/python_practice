#coding: utf-8
import requests
from bs4 import BeautifulSoup
# write Chinese character to file.
import codecs

f = 'test.txt'
i = 0

def write_file(url):
    responseText = requests.get(url).text
    soup = BeautifulSoup(responseText,'html.parser')
    with codecs.open(f, 'a', 'utf-8') as file:
        for txt in soup.find_all(class_='text'):
            contentList = txt.find_all('p')
            content = ''
            for con in contentList:
                content = content + con.get_text() + '\t'
            file.write(content + '\n')
            file.write('\n')

if __name__ == '__main__':
    previousPage = 'http://jandan.net/duan'
    while i < 2:
        write_file(previousPage)
        previousPage = BeautifulSoup(requests.get(previousPage).text,'html.parser').find(class_='previous-comment-page').get('href')
        i += 1


