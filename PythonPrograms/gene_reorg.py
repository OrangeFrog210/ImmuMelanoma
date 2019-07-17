"""
Reorganizes the GDAC Broad Institute RNA seq data into a form that can be run in CIBERSORTX.

LM: Jult 16th, 2019
"""
import re
fIn = "/home/yshiba/immu_melanoma/SKCM.SKCM.rnaseqv2__illuminahiseq_rnaseqv2__unc_edu__Level_3__RSEM_genes__data.data.txt"
fOut = "/home/yshiba/immu_melanoma/im_m_rnaseq_fb_notnormalized_intm_.csv"

with open(fOut, 'w') as fw:
    with open(fIn, 'r') as fr:
        line1 = fr.readline().strip()
        fw.write(line1 + '\n')

        for line in fr:
            line = line.strip()
            cut = '|' + line.split(',')[0].split('|')[1].strip()
            linenew = line.replace(cut, '')
            fw.writelines(linenew + '\n')
