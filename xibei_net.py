import time

import requests
from requests import RequestException
from tools import *

def search_url_3(url_main,filefolder,pre_url):
    headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    response = requests.get(url_main, headers=headers)
        # 加一个判断，判断请求URL是否成功
    if response.status_code == 200:
        response.encoding = "UTF-8"

        soup = BeautifulSoup(response.text, 'lxml')

        list_title=soup.select('table[class="winstyle59821"] > tr')

        for j in list_title:
            try:
                if "img" in j.attrs["id"]:
                    continue
                temp_url=j.find("a").attrs["href"]
                if "www" not in temp_url:
                    temp_url=pre_url+temp_url[2:]
                print(temp_url)

                get_one_page_3(temp_url,filefolder)
            except Exception:
                print("Exceprtion_2")

def get_one_page_3(url, filefolder):
    try:
        # 需要重置requests的headers。
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"}
        response = requests.get(url, headers=headers)
        # 加一个判断，判断请求URL是否成功
        if response.status_code == 200:
            response.encoding = "UTF-8"
            soup = BeautifulSoup(response.text, 'lxml')
            time.sleep(3)

            write_txt(filefolder, get_biaoti_3(soup), get_full_3(soup))
        response.close()

        return None
    except Exception:
        print("requestException")
        response.close()

        return None

def get_biaoti_3(soup):
    return soup.select('table[class="winstyle457865076_961"]>tr')[0].text

def get_full_3(soup):
    full_txt=""
    for i in soup.select('td[class="contentstyle457865076_961"]>div[id="vsb_content"]>p'):
        full_txt+=i.text


    return full_txt




def write_txt(filefolder,biaoti,full_text):
    biaoti=biaoti.strip()
    f=open(filefolder+'\\'+biaoti+".txt","w+",encoding='utf-8')
    f.write(biaoti+"\n")
    f.write(full_text)
    f.close()

#search_url_3("http://www.nw.sgcc.com.cn/zxzx/xw.htm","西北分部要闻","http://www.nw.sgcc.com.cn")

for k in range(170,0,-1):
    search_url_3("http://www.nw.sgcc.com.cn/zxzx/xw/"+str(k)+".htm", "西北分部要闻", "http://www.nw.sgcc.com.cn")
