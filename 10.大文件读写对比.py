#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :10.大文件读写对比.py
# @Time      :2022/11/21 15:17
# @Author    : https://github.com/TonyEinstein
import sys
import time
import pandas as pd
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import threading

def saveFile(file_writer,data_line,locker):
    locker.acquire()
    file_writer.write(",".join(data_line)+"\n")
    locker.release()

if __name__ == '__main__':

    df = pd.read_csv("大文件读写/韶关智成0110-0421_多秤_hour_details.csv")


    df = df.astype(str)
    data = np.array(df)
    data_list = data.tolist()
    #
    start_time = time.perf_counter()
    df.to_csv("大文件读写/1.csv", encoding="utf-8", index=False)
    # lock = threading.Lock()
    # executor = ThreadPoolExecutor()
    # with open("大文件读写/2.csv",mode="w",encoding="utf-8") as f:
    #     task = [executor.submit(saveFile, f, rline, lock) for rline in data_list]
    #     wait(task)
    # 获取结束时间，并计算花费的时间
    end_time = time.perf_counter() - start_time
    print(f'总共耗时{round(end_time, 2)}秒')












