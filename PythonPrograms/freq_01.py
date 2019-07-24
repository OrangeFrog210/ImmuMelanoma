"""

LM: July 23rd, 2019
"""
import pandas as pd

fIn_01 = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes-transposed.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_01freq.csv"

df = pd.read_csv(fIn_01)

with open(fOut, 'w') as fw:
    fw.writelines("geneName,mut1_count,not0_count,total\n")
    for col in df[1:]:
        count1, count0 = 0, 0
        mutated_1_list = df[df[col] == 1].official_gene_symbol.tolist()
        mutated_0_list = df[df[col] == 0].official_gene_symbol.tolist()
        #print(mutated_1_list), print(mutated_0_list)
        # print(len(mutated_1_list) + len(mutated_0_list))
        fw.writelines(col + ',' + str(len(mutated_1_list)) + ',' + str(len(mutated_0_list))  + ',' + str(len(mutated_1_list) + len(mutated_0_list)) + '\n')