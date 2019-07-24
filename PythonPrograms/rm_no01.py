"""
Matches the gene expression data with functional mutation status
(functionally mutated: 1, or wild type: 0)

LM: July 24th, 2019.
"""
import os
import glob


path = "/home/yshiba/immu_melanoma/matched/rest/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

for f in list_csvnames:
    geneName = f.split('.')[0].split('_')[11]
    print(geneName)
    fOut = f.split('.')[0] + "_labeled.csv"

    with open(fOut, 'w') as fw:
        fw.writelines("official_gene_symbol,geneExp,fxm01\n")
        with open(f, 'r') as fin:
            for line in fin:
                line = line.strip()
                if line.split(',')[-1] == '1':
                    fw.writelines(line + '\n')
                elif line.split(',')[-1] == '0':
                    fw.writelines(line + '\n')