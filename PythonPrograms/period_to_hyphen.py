"""
replaces any period in a file to hyphen ('.' to '-')

LM: July 23rd, 2019.
"""

fileIn = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes.csv"
fileOut = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes_-.csv"

with open(fileIn, 'r') as fin:
    with open(fileOut, 'w') as fw:
        for line1 in fin:
            line1 = line1.strip()
            line = line1.replace('.', '-')
            fw.writelines(line + "\n")