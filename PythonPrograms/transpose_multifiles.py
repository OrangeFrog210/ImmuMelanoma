"""
In each file, only keeps one type of gene that the file is chosen based on.
LM: July 23rd, 2019
"""
import os
import glob
import pandas as pd

path = "/home/yshiba/immu_melanoma/NK/1gene/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(list_csvnames)

for file in list_csvnames:
    geneName = file.split('_')[-2].split('.')[0]
    print(geneName)

    df = pd.read_csv(file)
    df.set_index("official gene symbol", inplace=True)
    #print(df)
    df_new = df.T
    print(df_new)
    fOut = file.split('.')[0] + "_T.csv"
    df_new.to_csv(fOut)
