import requests
from bs4 import BeautifulSoup


def get_html(url):  # 获取url源码
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    res = requests.get(url=url, headers=headers)
    res.encoding = res.apparent_encoding
    text = BeautifulSoup(res.text, 'lxml')
    return text


def hnu_page(): #湖南大学
    url = "http://csee.hnu.edu.cn/zsjy/sszs.htm"
    url_host = "http://csee.hnu.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def ustc_page():  #中国科学技术大学
    url = "https://yz.ustc.edu.cn/list_1.htm"
    url_host = "https://yz.ustc.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def zju_page():  #浙江大学
    url = "http://www.cst.zju.edu.cn/32178/list.htm"
    url_host = "http://www.cst.zju.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def hust_page():  #华中科技大学
    url = "http://cs.hust.edu.cn/zxtz/24.htm"
    url_host = "http://cs.hust.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def peking_page():  #北京大学
    url = "https://admission.pku.edu.cn/xly/index.htm?CSRFT=AQJ4-1F1G-N5T6-4SUM-YV8D-WCM1-LSWI-0Y2C"
    url_host = ""
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def nju_page():  #南京大学!!
    url = "https://software.nju.edu.cn//tzgg/index.html"
    url_host = ""
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def whu_page():  #武汉大学
    url = "http://cs.whu.edu.cn/news_list.aspx?category_id=54&page=2"
    url_host = "http://cs.whu.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def scu_page():  #四川大学!!
    url = "https://cs.scu.edu.cn/index/xytz/38.htm"
    url_host = "https://cs.scu.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info

def lzu_page():  #兰州大学!!
    url = "http://xxxy.lzu.edu.cn/tongzhigonggao/"
    url_host = "https://cs.scu.edu.cn"
    text = get_html(url)
    summer_info = {}
    change_info = {}

    infos = text.find_all('a')

    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url_host + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url_host + url_href
    return summer_info, change_info


info ={"湖大":hnu_page(),
       "中科大":ustc_page(),
       "浙大":zju_page(),
       "华科":hust_page(),
       "北大":peking_page(),
       "南大":nju_page(),
       "武大":whu_page(),
       "川大":scu_page(),
       "兰大":lzu_page()
       }  #记录院校对应的信息


def package_make(school_):
    dict_summer = {}
    dict_change = {}
    tuple_temp = info[school_]
    dict_summer[school_] = tuple_temp[0]
    dict_change[school_] = tuple_temp[1]
    print(dict_summer)
    print(dict_change)


if __name__ == "__main__":

    school = input("请输入目标大学：")  #例湖大
    package_make(school)