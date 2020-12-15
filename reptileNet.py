"""
中国电力建设集团有限公司
"""
from lxml import etree
import time

import requests
from requests import RequestException
from tools import *

#获取首页内容
def get_one_page(url,filefolder):

    try:
        # 需要重置requests的headers。
        headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        response = requests.get(url, headers=headers)
        # 加一个判断，判断请求URL是否成功
        if response.status_code == 200:
            response.encoding = "GBK"
            soup = BeautifulSoup(response.text, 'lxml')
            write_txt(filefolder,get_biaoti(soup),get_full(soup))

        return None
    except RequestException:
        print("requestException")
        return None

#东北
def get_one_page_2(url, filefolder):
    try:
        # 需要重置requests的headers。
        headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
        response = requests.get(url, headers=headers)
        # 加一个判断，判断请求URL是否成功
        if response.status_code == 200:
            response.encoding = "GBK"
            soup = BeautifulSoup(response.text, 'lxml')
            write_txt(filefolder, get_biaoti_2(soup), get_full_2(soup))

        return None
    except RequestException:
        print("requestException")
        return None


def get_biaoti(soup):

    return soup.select('div[class="con"]>h2')[0].text

def get_full(soup):
    full_txt=""
    for i in soup.select('div[class="con"]>div'):
        full_txt+=i.text
    return full_txt




# 华北前一部分
def search_url(url_main,filefolder,pre_url):
    headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url_main, headers=headers)

        # 加一个判断，判断请求URL是否成功
    if response.status_code == 200:
        response.encoding = "GBK"
        soup = BeautifulSoup(response.text, 'lxml')
        list_title=soup.select('div[class="listR"]>div[class="lb"]>dl')
        for j in list_title:
            temp_url=j.find("a").attrs["href"]
            if "www" not in temp_url:
                temp_url=pre_url+temp_url
            get_one_page(temp_url,filefolder)
# 东北
def search_url_2(url_main,filefolder,pre_url):
    headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url_main, headers=headers)
        # 加一个判断，判断请求URL是否成功
    if response.status_code == 200:
        response.encoding = "GBK"
        soup = BeautifulSoup(response.text, 'lxml')

        list_title=soup.select('div[class="SecConRB1"]>ul>li')
        print(len(list_title))
        print(list_title)
        for j in list_title:
            temp_url=j.find("a").attrs["href"]
            if "www" not in temp_url:
                temp_url=pre_url+temp_url[1:]

            get_one_page_2(temp_url,filefolder)

def get_one_page_2(url, filefolder):
    try:
        # 需要重置requests的headers。
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"}
        response = requests.get(url, headers=headers)
        # 加一个判断，判断请求URL是否成功
        if response.status_code == 200:
            response.encoding = "GBK"
            soup = BeautifulSoup(response.text, 'lxml')
            time.sleep(2)

            write_txt(filefolder, get_biaoti_2(soup), get_full_2(soup))
        response.close()

        return None
    except RequestException:
        print("requestException")
        response.close()

        return None

def get_biaoti_2(soup):

    return soup.select('div[class="thirdDetailsbt"]')[0].text

def get_full_2(soup):
    full_txt=""
    for i in soup.select('div[class="Custom_UnionStyle"]>p'):
        full_txt+=i.text
    return full_txt




def write_txt(filefolder,biaoti,full_text):
    biaoti=biaoti.strip()
    f=open(filefolder+'\\'+biaoti+".txt","w+",encoding='utf-8')
    f.write(biaoti+"\n")
    f.write(full_text)
    f.close()

#search_url("http://www.nc.sgcc.com.cn","华北分部要闻")
search_url_2("http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw/default_1.htm","东北分部要闻","http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw")
search_url_2("http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw/default.htm","东北分部要闻","http://www.ne.sgcc.com.cn/dbdwww/zxzx/gsxw")
#search_url("http://www.nc.sgcc.com.cn/zxzx/gsxw/index.shtml","华北分部要闻",pre_url="http://www.nc.sgcc.com.cn")



