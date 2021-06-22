#-*- codeing = utf-8 -*-
#@Time : 2021/6/1919:35
#@Author : 王静羚
#@File : pachong.py
#@Softwore:PyCharm
#爬虫，按照一定的规则，自动抓取互联网信息的程序和自动脚本，
# def main():
#     print("hello")
# if __name__=="__main__":
#     main()
# 引入模块 库
#

from bs4 import BeautifulSoup #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error #制定URL,获取网页数据
import xlwt #进行excle操作
import sqlite3 # 进行SQLite数据库操作
def main():

    baseurl="https://movie.douban.com/top250?start="
    datalist=getData(baseurl)
    savepath="豆瓣电影Top250.xls"

    # saveData(datalist,savepath)

findlink=re.compile(r'<a href="(.*?)">') #生成正则表达式的对象，表示规则（字符串的模式）
findimgsrc=re.compile(r'<img.*src="(.*?)"',re.S)# re.S让换行符包含在字符中
findtitle=re.compile(r'<span class="title">(.*)</span>')
findrating=re.compile(r'span class="rating_num" property="v:average">(.*)</span>')
findjudge=re.compile(r'<span>(\d*)人评价</span>')
findinq=re.compile(r'<span class="inq">(.*)</span>')
findbd=re.compile(r'<p class="">(.*?)</p>',re.S)

# 爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10): #调用获取页面的函数
        url=baseurl+str(i*25)
        html=askurl(url) #保存获取道德网页信息
    # 解析数据
    # 逐一解析
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            # print(item)
            data=[] #保存一部电影的信息
            item=str(item)
            # # 影片的链接
            link=re.findall(findlink,item)[0] #re库通过正则表达来指定字符串
            data.append(link)
            # print(link)

            imgsrc=re.findall(findimgsrc,item)[0]
            data.append(imgsrc)

            titles=re.findall(findtitle,item)
            if (len(titles)==2):
                ctitle=titles[0]
                data.append(ctitle)
                otitle=titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating=re.findall(findrating,item)[0]
            data.append(rating)

            judgenum=re.findall(findjudge,item)[0]
            data.append(judgenum)

            inq=re.findall(findinq,item)
            if len(inq)!=0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd=re.findall(findbd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd=re.sub('/'," ",bd)
            data.append(bd.strip())

            datalist.append((data))

    return datalist
#指定一个url的网页内容
def  askurl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    } # 用户代理告诉豆瓣我们是浏览器，不是爬虫。
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    return html
    # print(html)

    # 保存数据
def saveData(datalist,savepath):
    print(savepath)
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)
    col=("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)




if __name__=="__main__":
    main()
    print("爬取完毕！")