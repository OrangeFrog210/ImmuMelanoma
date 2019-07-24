"""
removes the first column, "geneName"
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
    df = pd.read_csv(f, sep='\t')
    df_new = df.drop(columns="geneName")
    print(df_new)
    fOut = f.split('.')[0] + "_drop.csv"
    df_new.to_csv(fOut, sep='\t', index=False)