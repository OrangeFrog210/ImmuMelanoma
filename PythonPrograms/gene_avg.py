"""
If multiple rows exist for a gene, then average each value in each column

LM: July 11th, 2019
"""
import pandas as pd
#import numpy as np

fIn = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_intm.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb.csv"

df = pd.read_csv(fIn, sep=',')
df_new = df.groupby(["geneName"]).mean()

df_new.to_csv(fOut, sep='\t')