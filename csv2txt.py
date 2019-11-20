import pandas as pd
import numpy as np

file_path = "/data/BaiDuBigData19-URFC/submit/multimodal_bestloss_submission.csv"
pf = pd.read_csv(file_path)

f = open("submit.txt","w+")
for i in  range(len(pf)):
    AreaID = pf.iloc[i]["Id"]
    CategoryID = pf.iloc[i]["Predicted"]
    f.write('%06d\t%03d\n' % (AreaID, CategoryID+1))
    if i % 1000 == 0:
        print('Step %d: area %s category %03d' % (i, AreaID, CategoryID))
f.close()





