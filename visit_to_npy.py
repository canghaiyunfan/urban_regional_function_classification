import math
import time
import numpy as np
import sys
import datetime
import pandas as pd
import os
import threading

from multiprocessing import cpu_count

# visit 数据转为 npy 格式，所需时间较长

# 用字典查询代替类型转换，可以减少一部分计算时间
date2position = {}
datestr2dateint = {}
str2int = {}
for i in range(24):
    str2int[str(i).zfill(2)] = i

# 访问记录内的时间从 2018年10月1日 到 2019年3月31日，共182天
# 将日期按日历排列
for i in range(182):
    date = datetime.date(day=1, month=10, year=2018) + datetime.timedelta(days=i)
    date_int = int(date.__str__().replace("-", ""))
    date2position[date_int] = [i % 7, i // 7]
    datestr2dateint[str(date_int)] = date_int

def visit2array(path, savepath, filenames):
    length = len(filenames)
    for index, filename in enumerate(filenames):
        table = pd.read_table(path + '/' + filename + '.txt', header=None)
        strings = table[1]
        init = np.zeros((7, 26, 24))
        for string in strings:
            temp = []
            for item in string.split(','):
                temp.append([item[0:8], item[9:].split("|")])
            for date, visit_lst in temp:
                # x - 第几天
                # y - 第几周
                # z - 几点钟
                # value - 到访的总人数
                x, y = date2position[datestr2dateint[date]]
                for visit in visit_lst:  # 统计到访的总人数
                    init[x][y][str2int[visit]] += 1
        np.save(savepath + "/" + filename + ".npy", init)
        print('%s: Processing visit data %d/%d' % (threading.current_thread().name, index + 1, length), end='\r')


def visit2array_mt(path, savepath, filename):
    table = pd.read_table(filename, header=None)
    filenames = [a[0].split("/")[-1].split('.')[0] for a in table.values]
    length = len(filenames)
    num_threads = 20 #cpu_count()
    len_per_thread = length // num_threads
    start_time = time.time()
    threads = []
    for ti in range(num_threads):
        fstart = ti * len_per_thread
        fend = length if ti == num_threads - 1 else (ti + 1) * len_per_thread
        t = threading.Thread(name='Thread-{}'.format(ti), target=visit2array,
                             args=[path, savepath, filenames[fstart:fend]])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    sys.stdout.write('\n')
    print("using time:%.2fs" % (time.time() - start_time))


if __name__ == '__main__':
    if not os.path.exists("/data/BaiDuBigData19-URFC/data/npy/test_visit/"):
        os.makedirs("/data/BaiDuBigData19-URFC/data/npy/test_visit/")
    if not os.path.exists("/data/BaiDuBigData19-URFC/data/npy/train_visit/"):
        os.makedirs("/data/BaiDuBigData19-URFC/data/npy/train_visit/")
    visit2array_mt('/data/BaiDuBigData19-URFC/data/train_part', '/data/BaiDuBigData19-URFC/data/npy/train_visit', "/data/BaiDuBigData19-URFC/data/train.txt")
    visit2array_mt('/data/BaiDuBigData19-URFC/data/train_part', '/data/BaiDuBigData19-URFC/data/npy/train_visit', "/data/BaiDuBigData19-URFC/data/valid.txt")
    visit2array_mt('/data/BaiDuBigData19-URFC/data/test_part', '/data/BaiDuBigData19-URFC/data/npy/test_visit', '/data/BaiDuBigData19-URFC/data/test.txt')