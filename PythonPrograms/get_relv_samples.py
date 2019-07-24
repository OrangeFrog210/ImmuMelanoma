"""
Gets the relevant samples in the mixture file.

LM: July 22nd, 2019
"""

fIn_relevant = "/home/yshiba/immu_melanoma/CIBERSORTxGEP_Job10_LM22_Fractions_NKactivated_th2pc.csv"
fIn = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_transp.csv"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_NKgenes_62_activated_transp_th2pc.csv"

with open(fIn_relevant, 'r') as fin_rel:
    list_relv_samples = []
    for line in fin_rel:
        eid = line.split(',')[0].strip()
        print(eid)
        list_relv_samples.append(eid)

print(len(list_relv_samples))


with open(fOut, 'w') as fw:
    with open(fIn, 'r') as fin:
        line = fin.readline().strip()
        fw.writelines(line + '\n')

        for line in fin:
            line = line.strip()
            geneName = line.split(',')[0].strip()
            if geneName in list_relv_samples:
                fw.writelines(line + '\n')
