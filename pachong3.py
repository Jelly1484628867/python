#-*- codeing = utf-8 -*-
#@Time : 2021/6/2021:14
#@Author : 王静羚
#@File : pachong3.py
#@Softwore:PyCharm
#  爬一个百度
'''
from urllib.request import urlopen
url="http://www.baidu.com"
response=urlopen(url)
# print(response.read().decode("utf-8"))
with open("mybaidu.html",mode='w') as f: #保存为一个html文件
    f.write(response.read().decode('utf-8'))# 从网页上读取到页面的源代码
print("over!")

'''

'''
import requests
url="https://www.ddxstxt8.com/1_1562/"
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}

response=requests.get(url,headers=headers)
print(response)
print(response.read().decode('utf-8')) #拿到网页源代码
'''
# 服务器渲染：在服务器那边直接靶数据和html整合在一起，统一返回给浏览器

# 客户渲染：第一次请求只要一个html的骨架，第二次请求拿到数据，进行数据展示
# 在页面源代码中看不到数据

# 熟练使用浏览器抓包工具
# http协议 超文本标记传输，传输网站的相关代码
# 请求
# 请求行：请求方式（post/url），
# 请求头（一些服务器使用的附加信息），
# 请求体（一般放请求参数）

# 响应
# 状态行
# 响应头
# 响应体
# 请求方式  get,post
'''
import requests
url="https://fanyi.baidu.com/sug"

s=input("请输入你要翻译的单词")
dat={
    "kw":s
}
#发送post的数据，必须放在字典中，同股派data参数进行传递
resp=requests.post(url,data=dat)
print(resp.json())# 将服务器返回的内容直接处理成json()
'''



import requests
url="https://movie.douban.com/j/chart/top_list"
param={
"type": "10",
"interval_id": "100:90",
"action":"",
"start": "0",
"limit": "20",
}
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
}
resp=requests.get(url=url,params=param,headers=header)
print(resp.json())
resp.close
