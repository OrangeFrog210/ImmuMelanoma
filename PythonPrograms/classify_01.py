"""

LM: July 23rd, 2019
"""
import pandas as pd

fIn_01 = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes-transposed.csv"
fIn_mixture = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_rest_transp_th2pc.csv"


df = pd.read_csv(fIn_01)

for col in df[1:]:

    mutated_1_list = df[df[col] == 1].official_gene_symbol.tolist()
    mutated_0_list = df[df[col] == 0].official_gene_symbol.tolist()
    print(mutated_1_list), print(mutated_0_list)
    #print(len(mutated_1_list) + len(mutated_0_list))
    print(col)  # contains the name of the gene

    with open(fIn_mixture, 'r') as finMix:
        with open("/home/yshiba/immu_melanoma/NK/im_m_rnaseq_fb_NK_62_1_%s.csv" % col, 'w') as fmut:
            with open("/home/yshiba/immu_melanoma/NK/im_m_rnaseq_fb_NK_62_0_%s.csv" % col, 'w') as fnotmut:
                line1 = finMix.readline().strip()
                fmut.writelines(line1 + '\n')
                fnotmut.writelines(line1 + '\n')
                for line in finMix:
                    line = line.strip()
                    pt0, pt1, pt2 = line.split('-')[0], line.split('-')[1], line.split('-')[2]
                    shorter_sampleID = pt0 + '-' + pt1 + '-' + pt2
                    print(shorter_sampleID)
                    if shorter_sampleID in mutated_1_list:
                        fmut.writelines(line + '\n')
                    elif shorter_sampleID in mutated_0_list:
                        fnotmut.writelines(line + '\n')