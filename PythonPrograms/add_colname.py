"""
adds "geneName" to every files for gene expression.
LM: July 24th, 2019.
"""

import os
import glob

path = "/home/yshiba/immu_melanoma/NK/1gene/Transposed/Tab/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

for file in list_csvnames:
    fOut = file.split('.')[0] + "_wn.csv"
    with open(file, 'r') as fin:
        with open(fOut, 'w') as fw:
            line1 = fin.readline().strip()
            fw.writelines("geneName\t" + line1 + '\n')
            for line in fin:
                line = line.strip()
                fw.writelines(line + '\n')


