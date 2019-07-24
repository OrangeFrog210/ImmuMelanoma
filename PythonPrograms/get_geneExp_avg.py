"""
Calcuates the gene expression average values of each of the gene + functional mutation condition
(functionally mutated or not)

LM: July 24th, 2019.
"""
import os
import glob
import pandas as pd
import numpy as np

fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NK_62_geneExp_avg.txt"
path = "/home/yshiba/immu_melanoma/log/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)
print(len(list_csvnames))

with open(fOut, 'w') as fw:
    fw.writelines("geneName,fxmut,avgGeneExp" + '\n')
    for f in list_csvnames:
        geneName = f.split('_')[8]
        fxnmut_state = f.split('_')[7]

        df = pd.read_csv(f, sep=',')
        arr = df.to_numpy()
        #print(arr)
        avg = np.mean(arr[0])
        print(avg)
        fw.writelines(geneName + ',' + fxnmut_state + ',' + str(avg) + '\n')