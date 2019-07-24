"""
In each file, only keeps one type of gene that the file is chosen based on.
LM: July 23rd, 2019
"""
import os
import glob
import pandas as pd

path = "/home/yshiba/immu_melanoma/NK/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(list_csvnames)

for file in list_csvnames:
    geneName = file.split('_')[-1].split('.')[0]
    print(geneName)

    df = pd.read_csv(file)
    df_new = df[['official gene symbol', geneName]]
    print(df_new)
    fOut = file.split('.')[0] + "_1gene.csv"
    df_new.to_csv(fOut, index=False)
