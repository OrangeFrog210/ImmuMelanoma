"""
Logs the gene expression profiles.
LM: July 24th, 2019.
"""

import os
import glob
import pandas as pd
import numpy as np

path = "/home/yshiba/immu_melanoma/wn/drop/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

count = 0
for f in list_csvnames:
    df = pd.read_csv(f, sep='\t')
    print(f)
    #print(df.dtypes)

    # removing any cell with value 0
    df_removed0 = df.loc[:, (df != 0).any(axis=0)]
    #print(df_removed0)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    # for c in [c for c in df_removed0.columns if df_removed0[c].dtype in numerics]:
    #     #print(np.log(df_removed0[c]))
    #     df_new = pd.DataFrame()
    df_new = np.log(df_removed0)

    print(df_new)
    fOut = f.split('.')[0] + '_log.csv'
    #print(fOut)
    count+= 1
    print(count)
    df_new.to_csv(fOut, index=False, sep=',')