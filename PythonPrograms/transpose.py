"""
Transposes a dataframe.
LM: July 23rd, 2019
"""
import pandas as pd

fIn = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_transp.csv"

df = pd.read_csv(fIn)
df_transposed = df.T

print(df_transposed)
df_transposed.to_csv(fOut)