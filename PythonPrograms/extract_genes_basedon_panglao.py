"""
Extracts the genes that seem to be
The x number of genes are taken based on the PanglaoDB databse.

LM: July 26th, 2019.
"""

fIn1 = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes_-.csv"
fIn2 = "/home/yshiba/immu_melanoma/panglaoDB_Bmem_Hs.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_BmemGenes_66.csv"


with open(fIn1, 'r') as fin1:
    listGenes = []
    for line in fin1:
        line = line.strip()
        genename = line.split(',')[0].strip()
        listGenes.append(genename)

print(listGenes)
print(len(listGenes))

with open(fOut, 'w') as fw:
    with open(fIn2, 'r') as fin2:
        for line2 in fin2:
            line2 = line2.strip()
            geneName = line2.split(',')[1].strip()
            print(geneName)
            # for element in listGenes:
            #     if element == geneName:
            #         fw.writelines(line2 + '\n')