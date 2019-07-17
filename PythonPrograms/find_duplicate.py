"""
If multiple rows exist for a gene, then average each value in each column

LM: July 11th, 2019
"""
import pandas as pd

fIn = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_intm.csv"

df = pd.read_csv(fIn, sep=',')
df_new = df.groupby(["geneName"]).mean()

gene = df["geneName"]
print(pd.concat(g for _, g in df.groupby("geneName") if len(g) > 1))