'''
伪装浏览器

对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。
具体实现：自定义网页请求报头。
'''

#实例二：依然爬取豆瓣，采用伪装浏览器的方式

import urllib.request
#网址
url = "https://www.douban.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
req = urllib.request.Request(url=url,headers=headers)

res = urllib.request.urlopen(req)

data = res.read()

data = data.decode('utf-8')

print(data)
#打印爬取网页的各类信息
print(type(res))
print(res.geturl())
print(res.info())
print(res.getcode())
