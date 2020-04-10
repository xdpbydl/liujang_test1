# -*- coding: utf-8 -*-
import requests
import json
import re
import os
from lxml import etree



def xima():
    m = 128            # 总条数（为1 时表示正序，从头至尾）
    mm = 0            # 1表示为正序,,0为倒序
    n = range(6,6)     # 判断没有下载完成的行号
    y = range(5)      # 页数
    d = 10191471        # 设置媒体文件在URL中的代码
    for i in y:
        url = 'https://www.ximalaya.com/revision/play/album?albumId={d}&pageNum={i}&sort=-1&pageSize=30'.format(d=d,i=i)
            #  https://www.ximalaya.com/revision/play/album?albumId=3385980&pageNum=9&sort=-1&pageSize=30
        headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Content-Type': 'text / html',
            'Referer': 'https://www.ximalaya.com/',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        ret = requests.get(url, headers=headers)

        r1 = ret.content.decode()
        r = json.loads(r1)
        list = r['data']['tracksAudioPlay']
        for i in list:
            name = i['trackName']
            src = i['src']
             #文件过多增加数字作为排序
            if len(str(m)) == 1:
                m = '00' + str(m)
            elif len(str(m)) == 2:
                m = '0' + str(m)
            name = re.sub ('\?|"|:|\|', '', name)   #  这个:须放在\前才有效？  而且\号存在多个，不能完全去除？？？
            file = 'E:/xima/{m}.{n}.m4a'.format (m=m, n=name)
            m = int (m)
            print(src, name)
            if m in n:  # 判断下载剩余条目
                #判断文件，如存在，不保存。
                if os.path.exists(file):
                    pass
                else :
                    with open(file, 'ab') as f:
                        music = requests.get(src, headers=headers)
                        f.write(music.content)
                        print (file + "______正在下载……")
            else:
                 print('第' + str(m) +  '条已经下载。')
            if mm == 1:  #正序时，变量加1，倒序时减1
                m += 1
            elif  mm == 0:
                m -= 1


# 提供下载音频ID  https://www.ximalaya.com/yinyue/18858975/
id = '/yinyue/18858975/'
url = 'https://www.ximalaya.com{}p1/'.format(id)


headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Content-Type': 'text / html',
    'Referer': 'https://www.ximalaya.com/',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}

# media_url = 'https://fdfs.xmcdn.com/group72/M0A/9A/5E/wKgO0F4gJWGxFmlaABu2PqFRNmc051.m4a'
# name = 'ddd'

def download(media_url, name):
    file = 'E:/xima/{}.m4a'.format(name)
    with open (file, 'ab') as f:
        mdeia = requests.get (media_url, headers=headers)
        f.write (mdeia.content)
        print (file + "______正在下载……")
# download(media_url, name)


def media_api(trackId):
    media_api_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(trackId)
    response = requests.get(media_api_url, headers=headers)
    data = response.json()
    src = data['data']['src']
    return src

# media_api('244461398')

def media_url(url):

   response = requests .get(url,headers=headers)
   title = '//*[@id="anchor_sound_list"]/div[2]/ul/li[1]/div[2]/a'
   # src =
   print(title)

   print(response.text,title)


media_url('https://www.ximalaya.com/youshengshu/24981038/')

