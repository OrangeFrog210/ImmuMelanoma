"""
Performs t-test.
LM: July 24th, 2019.
"""
import os
import glob
import pandas as pd
from scipy.stats import ttest_ind

fOut = "/home/yshiba/immu_melanoma/skcm_cadd12tag_NKgenes_rest_ttest_result.txt"
path = "/home/yshiba/immu_melanoma/matched/rest/labeled/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

with open(fOut, 'w') as fw:
    fw.writelines("geneName,tstats,pvalue\n")
    for f in list_csvnames:
        geneName = f.split('_')[11]
        df = pd.read_csv(f, sep=',')

        fxmutated = df[df['fxm01'] == 1]
        wild_type = df[df['fxm01'] == 0]
        result = ttest_ind(fxmutated['geneExp'], wild_type['geneExp'])
        fw.writelines(geneName + ',' + str(result[0]) + ',' + str(result[1]) + '\n')

