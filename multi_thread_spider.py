from requests import get
from requests.sessions import Session
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import time
from queue import Queue
from threading import Thread

def spider_all(up_name_list):
    up_list = []
    video_list = []
    count = 0
    for up_name in up_name_list:
        count += 1
        print(count)
        up_list.append(spider_up(name_to_mid(up_name)))
        #video_list.append(spider_up_video(up_list[-1]['videos'], up_list[-1]['mid']))
        time.sleep(0.2)
    up_data = pd.DataFrame(up_list)
    #video_data = pd.DataFrame(video_list)
    up_data.to_csv('up_data.csv', index = False)
    #video_data.to_csv('video_data.csv', index = False)



def name_to_mid(name):
    url = 'https://search.bilibili.com/upuser?keyword='+name
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    response = get(url, headers = {'User-Agent':ua})
    #print(response.text)
    data = response.content.decode()
    #print(BeautifulSoup(data, 'lxml'))
    node =  BeautifulSoup(data, 'lxml').find('a', class_='face-img')
    #print(node)
    mid = ''.join(re.findall(r'\d', node.get('href')))
    time.sleep(0.2)
    return mid

def spider_up(in_q, out_q):
    while in_q.empty() is not True:
        mid = in_q.get()
        print(mid)
        url = 'https://api.bilibili.com/x/space/upstat?mid='+mid+'&jsonp=jsonp'
        url2 = 'https://api.bilibili.com/x/relation/stat?vmid='+mid+'&jsonp=jsonp'
        url_video = 'https://api.bilibili.com/x/space/arc/search?mid='+mid+'&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

        response = get(url, headers = {'User-Agent':ua})
        response2 = get(url2, headers = {'User-Agent':ua})
        response3 = get(url_video, headers = {'User-Agent':ua})
        info_up1 = eval(response.text)
        info_up2 = eval(response2.text)
        info_videos = eval(response3.text.replace('false', 'False'))

        up_dict = {}
        up_dict['view'] = info_up1['data']['archive']['view']
        up_dict['likes'] = up_dict['likes'] = info_up1.get('data').get('likes')
        up_dict['mid'] = mid
        up_dict['follower'] = info_up2.get('data').get('follower')
        #print(info_videos)
        pages = info_videos['data']['page']['count'] // info_videos['data']['page']['ps'] + 1

        video_list = []
        for pn in range(pages):
            url_page = 'https://api.bilibili.com/x/space/arc/search?mid='+mid+'&ps=30&tid=0&pn='+str(pn+1)+'&keyword=&order=pubdate&jsonp=jsonp'
            response3 = get(url_page, headers = {'User-Agent':ua})
            info_videos = eval(response3.text.replace('false', 'False').replace('true', 'True').replace('null', '"NaN"'))
            for elem in info_videos['data']['list']['vlist']:
                video_list.append((elem['bvid'], elem['length']))
                time.sleep(0.2)
        up_dict['videos'] = video_list
        out_q.put(up_dict)
        in_q.task_done()




def spider_video(in_q, out_q):
    #爬取视频基本信息
    while in_q.empty() is not True:
        elem = in_q.get()
        bvid, length = elem[0], elem[1]
        #print(bvid)
        url = 'https://api.bilibili.com/x/web-interface/view?bvid='+bvid
        ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
        response = get(url, headers = {'User-Agent':ua})
        print(response.text)
        info = eval(response.text.replace('false', 'False').replace('true', 'True').replace('null', '"NaN"'))
        if(info['code'] != 0):
            in_q.task_done()
            continue
        video_info = {}
        video_info['bvid'] = bvid
        video_info['owner'] = info['data']['owner']['mid']
        video_info['type'] = info['data']['tid']
        video_info['type_name'] = info['data']['tname']
        video_info['title'] = info['data']['title']
        video_info['view'] = info['data']['stat']['view']
        video_info['favorite'] = info['data']['stat']['favorite']
        video_info['coin'] = info['data']['stat']['coin']
        video_info['share'] = info['data']['stat']['share']

        #爬取视频发布时间
        url2 = 'https://www.bilibili.com/video/'+bvid
        response = get(url2, headers={'User-Agent': ua})
        data = response.content.decode()
        node = BeautifulSoup(data, 'lxml').find('meta', itemprop = 'uploadDate')
        if(node == None):
            in_q.task_done()
            continue
        else:
            video_info['time'] = node.get('content')
        video_info['length'] = length
        time.sleep(0.5)
        out_q.put(video_info)

        in_q.task_done()


def spider_and_store_up():
    up_name_list = list(pd.read_excel('up_data.xlsx')['昵称'].values)
    queue = Queue()
    result_queue = Queue()
    for up_name in up_name_list:
        print(up_name)
        queue.put(name_to_mid(up_name))

    for index in range(20):
        thread = Thread(target=spider_up, args=(queue, result_queue,))
        thread.daemon = True
        thread.start()
    queue.join()

    up_list = []
    while result_queue.empty() is not True:
        up_list.append(result_queue.get())
    up_data = pd.DataFrame(up_list)
    up_data.to_csv('up_data.csv', index=False)

def spider_and_store_videos():
    queue = Queue()
    result_queue = Queue()
    up_data = pd.read_csv('up_data.csv')
    for i in range(100):
        for elem in eval(up_data.loc[i]['videos']):
            queue.put(elem)


    for index in range(12):
        thread = Thread(target=spider_video, args=(queue, result_queue,))
        thread.daemon = True
        thread.start()

    queue.join()

    video_list = []
    while result_queue.empty() is not True:
        video_list.append(result_queue.get())
    video_data = pd.DataFrame(video_list)
    video_data.to_csv('video_data.csv', index=False)


if __name__ == '__main__':
    #spider_and_store_up()
    spider_and_store_videos()



