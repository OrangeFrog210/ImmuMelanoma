"""
replaces any period in a file to hyphen ('.' to '-')

LM: July 23rd, 2019.
"""
import os
import glob

path = "/home/yshiba/immu_melanoma/NK/1gene/Transposed/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

for file in list_csvnames:
    fOut = file.split('.')[0] + '_tab.csv'
    with open(file, 'r') as fin:
        with open(fOut, 'w') as fw:
            for line1 in fin:
                line1 = line1.strip()
                line = line1.replace(',', '\t')
                fw.writelines(line + "\n")