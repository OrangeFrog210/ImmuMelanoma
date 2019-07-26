"""
Adds "sampleID" and "logGeneExp" in the first column as index.
"""
import os
import glob

path = "/home/yshiba/Redo_activated/tab/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(list_csvnames)

for f in list_csvnames:
    fOut = f.split('.')[0] + "_index.csv"
    with open(fOut, 'w') as fw:
        with open(f, 'r') as fin:
            line1 = fin.readline().strip()
            line2 = fin.readline().strip()
            fw.writelines("sampleID," + line1 + '\n')
            fw.writelines("logGeneExp," + line2 + '\n')