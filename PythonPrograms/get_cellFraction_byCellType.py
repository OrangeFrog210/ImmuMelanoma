"""
and cuts any samples that are values less than 0.02.
LM: July 26th, 2019.
"""
import pandas as pd
fIn = "/home/yshiba/immu_melanoma/CIBERSORTxGEP_Job10_LM22_Fractions.csv"

df = pd.read_csv(fIn, sep='\t')
columns = list(df)
columns.remove("sampleID")
columns.remove("P-value")
columns.remove("Correlation")
columns.remove("RMSE")

print(columns)

for i in columns:
    df_new = df[["sampleID", i]]
    df_th002 = df_new[~(df_new[i] < 0.02)]
    print(df_th002)
    new_name = i.replace(' ', '_')
    fOut = "/home/yshiba/immu_melanoma/skcm_LM22_frac_th0.02_%s.csv" % new_name
    print(fOut)
    df_th002.to_csv(fOut, sep='\t', index=False)

