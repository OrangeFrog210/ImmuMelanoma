"""
adds the first column, "geneName"
LM: July 24th, 2019.
"""

import os
import glob
import pandas as pd

path = "/home/yshiba/immu_melanoma/wn/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))
for f in list_csvnames:
    geneName = f.split('_')[8]
    print(geneName)
    fOut = f.split('.')[0] + 'geneName.csv'
    with open(f, 'r') as fin:
        with open(fOut, 'w') as fw:
            line1 = fin.readline().strip()
            line2 = fin.readline().strip()
            fw.writelines("geneName\t" + line1 + '\n')
            fw.writelines(geneName + '\t' + line2 + '\n')