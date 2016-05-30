'''
program: csdn博文爬虫
function: 实现对我的csdn主页所有博文的日期、主题、访问量、评论个数信息爬取

version: python 3.5.1
time: 2016/05/29
author: yr
'''

import urllib.request,re,time,random,gzip

#定义保存文件函数
def saveFile(data,i):
    path = "E:\\projects\\Spider\\05_csdn\\papers\\paper_"+str(i+1)+".txt"
    file = open(path,'wb')
    page = '当前页：'+str(i+1)+'\n'
    file.write(page.encode('gbk'))
    #将博文信息写入文件(以utf-8保存的文件声明为gbk)
    for d in data:
        d = str(d)+'\n'
        file.write(d.encode('gbk'))
    file.close()

#解压缩数据
def ungzip(data):
    try:
        #print("正在解压缩...")
        data = gzip.decompress(data)
        #print("解压完毕...")
    except:
        print("未经压缩，无需解压...")
    return data

#CSDN爬虫类
class CSDNSpider:
    def __init__(self,pageIdx=1,url="http://blog.csdn.net/fly_yr/article/list/1"):
        #默认当前页
        self.pageIdx = pageIdx
        self.url = url[0:url.rfind('/') + 1] + str(pageIdx)
        self.headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Host": "blog.csdn.net"
        }

    #求总页数
    def getPages(self):
        req = urllib.request.Request(url=self.url, headers=self.headers)
        res = urllib.request.urlopen(req)

        # 从我的csdn博客主页抓取的内容是压缩后的内容，先解压缩
        data = res.read()
        data = ungzip(data)
        data = data.decode('utf-8')

        pages = r'<div.*?pagelist">.*?<span>.*?共(.*?)页</span>'
        #link = r'<div.*?pagelist">.*?<a.*?href="(.*?)".*?</a>'
        # 计算我的博文总页数
        pattern = re.compile(pages, re.DOTALL)
        pagesNum = re.findall(pattern, data)[0]
        return pagesNum

    #设置要抓取的博文页面
    def setPage(self,idx):
        self.url = self.url[0:self.url.rfind('/')+1]+str(idx)

    #读取博文信息
    def readData(self):
        ret=[]
        str = r'<dl.*?list_c clearfix">.*?date_t"><span>(.*?)</span><em>(.*?)</em>.*?date_b">(.*?)</div>.*?'+\
              r'<a.*?set_old">(.*?)</a>.*?<h3.*?list_c_t"><a href="(.*?)">(.*?)</a></h3>.*?'+\
              r'<div.*?fa fa-eye"></i><span>\((.*?)\)</span>.*?fa-comment-o"></i><span>\((.*?)\)</span></div>'
        req = urllib.request.Request(url=self.url, headers=self.headers)
        res = urllib.request.urlopen(req)

        # 从我的csdn博客主页抓取的内容是压缩后的内容，先解压缩
        data = res.read()
        data = ungzip(data)
        data = data.decode('utf-8')
        pattern = re.compile(str,re.DOTALL)
        items = re.findall(pattern,data)
        for item in items:
            ret.append(item[0]+'年'+item[1]+'月'+item[2]+'日'+'\t'+item[3]+'\n标题：'+item[5]
                       +'\n链接：http://blog.csdn.net'+item[4]
                       +'\n'+'阅读：'+item[6]+'\t评论：'+item[7]+'\n')
        return ret

#定义爬虫对象
cs = CSDNSpider()
#求取
pagesNum = int(cs.getPages())
print("博文总页数： ",pagesNum)

for idx in range(pagesNum):
    cs.setPage(idx)
    print("当前页：",idx+1)
    #读取当前页的所有博文，结果为list类型
    papers = cs.readData()
    saveFile(papers,idx)




