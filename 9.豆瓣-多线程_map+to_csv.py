#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :9.豆瓣-多线程_as_completed.py
# @Time      :2022/11/21 9:46
# @Author    : https://github.com/TonyEinstein

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :
# @Time      :2022/11/19 16:11
# @Author    : https://github.com/TonyEinstein
import time

import requests
import logging
import json
from lxml import etree
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
'''
获取数据分析所需的字段内容
抓取字段：影片名，最终评分，五星、四星、三星、二星、一星
抓取的startURL:  
'''
def getUrl(i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    logging.captureWarnings(True) #关闭多余的警告信息
    datas = []  # 所有数据将加入这里
    #确定起始URL
    urls = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={}'.format(i)
    try:
        responses = requests.get(urls,headers=headers,timeout=5,verify=False)  # verify=False，不验证证书
        if responses.status_code == 200:
            #如果起始URL响应正常，打印一下信息
            print('成功连接： ', urls)
            responsesDict = json.loads(responses.text)
            for dicts in responsesDict['data']:
                url = dicts['url']
                try:
                    response = requests.get(url, headers=headers, timeout=5, verify=False)
                    response.encoding = 'utf-8'
                    if response.status_code == 200: #对是否有正常的响应 加入判断
                        #如果url响应正常打印如下信息
                        print("子网页链接成功： ", url, ' 链接状态 ：', response.status_code, '正在等待解析.....')
                        html = etree.HTML(response.text)
                        #使用xpath进行解析
                        movie_Name_Year = html.xpath('//*[@id="content"]/h1/span/text()')
                        movie_Score = html.xpath(
                            '//*[@id="interest_sectl"]//div[@class="rating_self clearfix"]/strong/text()')
                        movie_Star = html.xpath(
                            '//*[@id="interest_sectl"]//div[@class="ratings-on-weight"]/div[@class="item"]/span[@class="rating_per"]/text()')

                        item = [movie_Name_Year[0], movie_Score[0], movie_Star[0], movie_Star[1], movie_Star[2],
                                movie_Star[3], movie_Star[4]]
                        print('解析成功!')
                        # 名字 电影评分  五星 四星 三星 二星 一星
                        datas.append(item)  # 添加数据到datas列表
                    else:
                        print("子网页链接失败： ", url, ' 链接状态 ：', response.status_code, '链接失败.....')
                except:
                    #url没有正常响应
                    print("子网链接失败:  ",url)
        else:
            print("网页链接失败： ", urls, ' 链接状态 ：', responses.status_code, '链接失败.....')
    except:
        #起始URL没有返回正常响应
        print('当前urls:  ', urls, '  未响应！')
    return datas

def saveFile(datas):

    dataColums = ['影片名', '最终评分', '五星', '四星', '三星', '二星', '一星']
    # 将数据转成Dataframe
    files = pd.DataFrame(columns=dataColums, data=datas)
    files.to_csv(r'data2.csv', index=False, encoding="utf-8")  # =保存到文件
    # 成功保存到文件后，打印输出done!提示
    print("done!")


def main():
    # 获取数据
    upLimit = 80
    executor = ThreadPoolExecutor()
    limit_list = [i for i in range(0, upLimit, 20)]
    results = executor.map(getUrl, limit_list)


    data = []
    # 保存数据
    for result in results:
        data = data+result
    saveFile(data)


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    # 获取结束时间，并计算花费的时间
    end_time = time.perf_counter() - start_time
    print(f'总共耗时{round(end_time, 2)}秒')




