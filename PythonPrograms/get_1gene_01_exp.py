"""
Separate the gene expression file by gene. Will create 62 files in total.
LM: July 24th, 2019.
"""
import pandas as pd

fIn_01 = "/home/yshiba/immu_melanoma/skcm_cadd12tag_t_order_NKgenes-transposed.csv"
fIn_mix = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_rest_transp_th2pc.csv"

df = pd.read_csv(fIn_01, sep=',')

# for col in df[1:]:
#     geneName = df[col].name
#     df_new = df[["official_gene_symbol", geneName]]
#     print(df_new)
#     df_new.to_csv("/home/yshiba/immu_melanoma/mut_01/skcm_cadd12tag_t_order_NKgenes_T_%s.csv" %geneName, sep=',', index=False)


df = pd.read_csv(fIn_mix, sep=',')
for col in df[1:]:
    geneName = df[col].name
    df_new = df[["official_gene_symbol", geneName]]
    print(df_new)
    df_new.to_csv("/home/yshiba/immu_melanoma/geneExp/im_m_rnaseq_fb_NKgenes_62_rest_transp_th2pc_%s.csv" %geneName, sep=',', index=False)