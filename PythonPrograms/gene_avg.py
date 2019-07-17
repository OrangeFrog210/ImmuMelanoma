"""
If multiple rows exist for a gene, then average each value in each column

LM: July 17th, 2019
"""
import pandas as pd

fIn = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_ntnorm_intm_.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_ntnorm_fb.csv"

df = pd.read_csv(fIn, sep=',')

print(df.dtypes)

df_new = df.groupby(["geneName"]).mean()

df_new.to_csv(fOut, sep='\t')
