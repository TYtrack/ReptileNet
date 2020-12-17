"""
北极星电力网首页
"""
from lxml import etree
import time

import requests
from requests import RequestException

import urllib.error
import urllib.request

from bs4 import BeautifulSoup 

# 东北
def search_url_10(url_main,filefolder,pre_url):
    headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url_main, headers=headers)
        # 加一个判断，判断请求URL是否成功
    if response.status_code == 200:
        response.encoding = "GBK"
        soup = BeautifulSoup(response.text, 'lxml')

        list_title=soup.select('ul[class="list_left_ul"]>li')

        for j in list_title:
            try:
                temp_url=j.find("a").attrs["href"]
                '''
                if "www" not in temp_url:
                    temp_url=pre_url+temp_url[1:]
                '''

                get_one_page_10(temp_url,filefolder)
            except Exception:
                print("false")
            

def get_one_page_10(url, filefolder):
    try:
        # 需要重置requests的headers。
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"}
        response = requests.get(url, headers=headers)
        
        # 加一个判断，判断请求URL是否成功
        if response.status_code == 200:
            response.encoding = "GBK"
            soup = BeautifulSoup(response.text, 'lxml')

            write_txt(filefolder, get_biaoti_10(soup), get_full_10(soup))
        response.close()

        return None
    except RequestException:
        print("requestException")
        response.close()

        return None

def get_biaoti_10(soup):
    s1=soup.select('div[class="list_detail"]>h1')[0].text
    #print(s1)
    return s1

def get_full_10(soup):
    full_txt=""
    zz=soup.find("div",attrs={"class":"list_detail"}).find_all("p")

    for i in zz:
        full_txt+=i.text
    return full_txt




def write_txt(filefolder,biaoti,full_text):
    biaoti=biaoti.strip()
    f=open("C:/Users/HUST/Desktop/中孚项目/项目/"+biaoti+".txt","w+",encoding='utf-8')
    f.write(biaoti+"\n")
    f.write(full_text)
    f.close()


for k in range(300):
    search_url_10("https://shupeidian.bjx.com.cn/NewsList?id=103&page="+str(k),"项目","https://news.bjx.com.cn/")
#search_url("http://www.nc.sgcc.com.cn","华北分部要闻")
#search_url_2("http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw/default_1.htm","东北分部要闻","http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw")
#search_url_2("http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw/default.htm","东北分部要闻","http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw")
#search_url("http://www.nc.sgcc.com.cn/zxzx/gsxw/index.shtml","华北分部要闻",pre_url="http://www.nc.sgcc.com.cn")





