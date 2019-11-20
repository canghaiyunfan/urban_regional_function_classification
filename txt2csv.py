import numpy as np
import pandas as pd

import csv

# with open('/data/BaiDuBigData19-URFC/data/train.csv', 'w+', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, dialect='excel')
#     # 读要转换的txt文件，文件每行各词间以字符分隔
#     with open('/data/BaiDuBigData19-URFC/data/train.txt', 'r', encoding='utf-8') as filein:
#         spamwriter.writerow(["Id", "Target"])
#         for line in filein:
#             # '/data/BaiDuBigData19-URFC/data/train/001/351285_001.jpg\n'
#             line_list = line.strip('\n').split('/')
#             id = line_list[-2] + '/' + line_list[-1][:-4]
#             target = int(line_list[-2])-1
#             spamwriter.writerow([id,target])
#
# with open('/data/BaiDuBigData19-URFC/data/test.csv', 'w+', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, dialect='excel')
#     # 读要转换的txt文件，文件每行各词间以字符分隔
#     with open('/data/BaiDuBigData19-URFC/data/test.txt', 'r', encoding='utf-8') as filein:
#         spamwriter.writerow(["Id", "Target"])
#         for line in filein:
#             # '/data/BaiDuBigData19-URFC/data/train/001/351285_001.jpg\n'
#             line_list = line.strip('\n').split('/')
#             id = line_list[-1][:-4]
#             target = 0
#             spamwriter.writerow([id,target])

with open('/data/BaiDuBigData19-URFC/data/train_oversampling.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, dialect='excel')
    # 读要转换的txt文件，文件每行各词间以字符分隔
    with open('/data/BaiDuBigData19-URFC/data/train_oversampling.txt', 'r', encoding='utf-8') as filein:
        spamwriter.writerow(["Id", "Target"])
        for line in filein:
            # '/data/BaiDuBigData19-URFC/data/train/001/351285_001.jpg\n'
            line_list = line.strip('\n').split('/')
            id = line_list[-2] + '/' + line_list[-1][:-4]
            target = int(line_list[-2])-1
            spamwriter.writerow([id,target])