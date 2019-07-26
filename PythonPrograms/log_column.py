"""
Logs the gene expression profiles which is in a column with
the name of the gene being the column name.
LM: July 245h, 2019.
"""

import os
import glob
import pandas as pd
import numpy as np

path = "/home/yshiba/Redo_activated/01TGT/Col_renamed/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

for f in list_csvnames:
    fOut = f.split('.')[0] + "_log.csv"
    geneName = f.split('.')[0].split('_')[10]
    print(geneName)
    df = pd.read_csv(f, sep=',')
    df['LogGeneExp'] = np.log(df.GeneExp)
    print(df)
    df.to_csv(fOut, sep=',', index=False)
