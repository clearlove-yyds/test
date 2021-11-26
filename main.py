
import requests
from bs4 import BeautifulSoup


def get_html(url):  # 获取url源码
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    res = requests.get(url=url, headers=headers)
    res.encoding = res.apparent_encoding
    text = res.text
    return text

def hnu_page(text, url): #湖南大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    #print(soup)
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info

def uestc_page(text, url): #电子科技大学 ！！
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    #print(soup)
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info

def hust_page(text, url): #华中科技大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info

def bupt_page(text, url): #北京邮电大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info

def zju_page(text, url): #浙江大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    print(soup)
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info


def ustc_page(text, url):  #中科大咨询获取
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')

    infos = soup.find_all('a')
    #print(type(infos))
    for info in infos:
        title = info.text
        url_href = info.get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href
    return summer_info, change_info


def peking_page(text, url): #北京大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')
    div_list = soup.find('div', class_='zsxx_cont_r fr')
    # print(div_list)
    li_list = div_list.find('ul', class_='zsxx_cont_list')
    li_list = li_list.find_all('li')
    for info in li_list:
        #title = info.find('a').find('p').string
        title = info.text
        url_href = info.find('a').get('href')
        if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "信息" in title:
            if "2021" in title:
                summer_info[title] = url_href
    return summer_info, change_info


def tsinghua_page(text, url):  #清华大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')
    infos = soup.find_all('div', class_='list03')
    for inf in infos:
        info = inf.find_all('a')
        for i in info:
            url_href = i.get('href')
            title = i.get('title')
            print(url_href[2:])
            print(title)
            if "调剂" in title:
                if "2021" in title:
                    change_info[title] = url + url_href[2:]
            elif "夏令营" in title:
                if "2021" in title:
                    summer_info[title] = url + url_href[2:]
                    #print(summer_info[title])
                    #print(url_href[2:])
                    #print(title)
    return summer_info, change_info


def nudt_page(text, url):  #国防科技大学
    summer_info = {}
    change_info = {}
    soup = BeautifulSoup(text, 'lxml')
    infos = soup.find('div', class_='news-list fl')
    infos = infos.find_all('li')
    # print(infos)
    for info in infos:
        title = info.find('h3').text
        url_href = info.find('a').get('href')
        print(title)
        print(url_href)
        '''if "调剂" in title:
            if "2021" in title:
                change_info[title] = url + url_href
        elif "夏令营" in title:
            if "2021" in title:
                summer_info[title] = url + url_href'''
    return summer_info, change_info

def package_make(school_, url, url_host, dict_summer_, dict_change_):
    if school_ == "中科大":
        tuple_temp = ustc_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "北大":
        tuple_temp = peking_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "清华":
        tuple_temp = tsinghua_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "国科大":
        tuple_temp = nudt_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "北邮":
        tuple_temp = bupt_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "浙大":
        tuple_temp = zju_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "华科":
        tuple_temp = hust_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "成电":
        tuple_temp = uestc_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]
    elif school_ == "湖大":
        tuple_temp = hnu_page(get_html(url), url_host)
        dict_summer_[school_] = tuple_temp[0]
        dict_change_[school_] = tuple_temp[1]

if __name__ == "__main__":
    dict_summer = {}
    dict_change = {}
    url0 = "https://yz.uestc.edu.cn/zsxc1/xly.htm"
    url1 = "https://yz.uestc.edu.cn"

    school = "成电"
    package_make(school, url0, url1, dict_summer, dict_change)
    print(dict_summer)
    print(dict_change)

    '''url0 = "https://admission.pku.edu.cn/xly/index.htm?CSRFT=AQJ4-1F1G-N5T6-4SUM-YV8D-WCM1-LSWI-0Y2C"  #
        url1 = "https://yz.ustc.edu.cn"
        school = "北大"
        package_make(school, url0, url1, dict_summer, dict_change)'''

    '''url0 = "https://www.cs.tsinghua.edu.cn/zszp/zsxx.htm"  #
    url1 = "https://www.cs.tsinghua.edu.cn"
    school = "清华"
    package_make(school, url0, url1, dict_summer, dict_change)
    print(dict_summer)'''

    '''url0 = "http://yjszs.nudt.edu.cn//pubweb/homePageList/searchContent.view"  #
    url1 = "https://www.cs.tsinghua.edu.cn"
    school = "国科大"
    package_make(school, url0, url1, dict_summer, dict_change)'''

    '''url0 = "http://cs.hust.edu.cn/zxtz/24.htm"  #
    url1 = "http://cs.hust.edu.cn"
    school = "华科"
    package_make(school, url0, url1, dict_summer, dict_change)'''

    '''url0 = "http://www.cst.zju.edu.cn/32178/list.htm"  #
    url1 = "http://www.cst.zju.edu.cn"
    school = "浙大"
    package_make(school, url0, url1, dict_summer, dict_change)'''

    '''url0 = "https://scs.bupt.edu.cn/rcpy1/yjspy.htm"  #
    url1 = "https://scs.bupt.edu.cn"
    school = "北邮"
    package_make(school, url0, url1, dict_summer, dict_change)'''

    '''url0 = "http://csee.hnu.edu.cn/zsjy/sszs.htm"  #
    url1 = "http://csee.hnu.edu.cn"
    school = "湖大"
    package_make(school, url0, url1, dict_summer, dict_change)'''