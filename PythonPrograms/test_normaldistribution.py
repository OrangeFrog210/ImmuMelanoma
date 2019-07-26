"""
Checks for normal distribution of the gene expression data of each of the gene.
LM: July 24th, 2019.
"""
import os
import glob
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NK_62_normdist_act.txt"
path = "/home/yshiba/Redo_activated/tab/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

with open(fOut, 'w') as fw:
    fw.writelines("geneName,fxmut,pValue" + '\n')
    for file in list_csvnames:
        geneName = file.split('_')[9]
        fxnmut_state = file.split('_')[7]
        #label = geneName + '_' + fxnmut_state

        df = pd.read_csv(file, sep=',')
        arr = df.to_numpy()
        arr_size = arr.size
        if arr_size > 8:
            #print(arr)
            #print(arr[0])
            cmp = np.random.normal(size=arr_size)

            #plt.hist(arr[0])
            #plt.show()
            #print(cmp)
            x = np.concatenate((cmp, arr[0]))
            print(x)
            k2, p = stats.normaltest(x)
            print(k2, p)
            fw.writelines(geneName + ',' + fxnmut_state + ',' + str(p) + '\n')