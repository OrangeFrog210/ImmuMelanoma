"""
Outputs csv files which each contains the genes that are important for
LM: July 26th, 2019.
"""
import pandas as pd
fIn = "/home/yshiba/immu_melanoma/PanglaoDB_markers.tsv"

df = pd.read_csv(fIn, sep='\t')
df_th01 = df[~(df["ubiquitousness index"] < 0.1)]
#print(df_th01)
df_Hs = df_th01[df_th01["species"].str.contains("Hs")]
#print(df_Hs)
df_new = df[["official gene symbol", "cell type"]]
#print(df_new)
for i, g in df_new.groupby("cell type"):
    #print(g)
    cell_name = g.iloc[0,1]
    cell_name_new = cell_name.replace(' ', '_')
    cell_name_final = cell_name_new.replace('/', 'OR')
    print(cell_name_final)
    g.to_csv("/home/yshiba/immu_melanoma/PanglaoDB_markers_UIth0.1_%s.tsv" % cell_name_final, sep='\t', index=False)