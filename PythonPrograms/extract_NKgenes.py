"""
Extracts the genes that seem to be
The 73 genes are taken based on the PanglaoDB databse.

LM: July 23rd, 2019.
"""

fIn1 = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes_-.csv"
fIn2 = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62.csv"


with open(fIn1, 'r') as fin1:
    listNKgenes = []
    for line in fin1:
        line = line.strip()
        genename = line.split(',')[0].strip()
        listNKgenes.append(genename)

print(listNKgenes)
print(len(listNKgenes))

with open(fOut, 'w') as fw:
    with open(fIn2, 'r') as fin2:
        for line2 in fin2:
            line2 = line2.strip()
            geneName = line2.split(',')[0].strip()
            print(geneName)
            for element in listNKgenes:
                if element == geneName:
                    fw.writelines(line2 + '\n')