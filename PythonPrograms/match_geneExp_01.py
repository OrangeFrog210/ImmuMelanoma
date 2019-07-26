"""
Matches the gene expression data with functional mutation status
(functionally mutated: 1, or wild type: 0)

LM: July 25th, 2019.
"""
import os
import glob


path = "/home/yshiba/immu_melanoma/mut_01/"
condition = "*.csv"
dir_condition = os.path.join(path, condition)
list_csvnames = []
for file in glob.glob(dir_condition):
    list_csvnames.append(file)

print(len(list_csvnames))

for file01 in list_csvnames:
    geneName = file01.split('.')[0].split('_')[8]
    #print(geneName)
    #file_GE = "/home/yshiba/Redo_activated/T/im_m_rnaseq_fb_NK_62_0_act_" + geneName + "_1gene_T_tabgeneName_drop_log_index_T_smpID.csv"
    file_GE = "/home/yshiba/Redo_activated/01TGT/Col_renamed/log/im_m_rnaseq_fb_NKgenes_62_act_transp_th2pc_" + geneName + "_smpID_log.csv"
    fOut = "/home/yshiba/Redo_activated/im_m_rnaseq_fb_NKgenes_62_act_transp_th2pc_01_" + geneName + ".csv"
    # Dictionary for 01
    with open(file01, 'r') as fin1:
        dict01 = {}
        next(fin1)
        for line1 in fin1:
            geneSymbol = line1.split(',')[0].strip()
            fxm01 = line1.split(',')[1].strip()

            dict01[geneSymbol] = fxm01

    with open(fOut, 'w') as fw:
        with open(file_GE, 'r') as fin2:
            line2 = fin2.readline().strip()
            fw.writelines(line2 + ",fxm01\n")

            for line1 in fin2:
                line1 = line1.strip()
                #geneSymbolExp = line1.split(',')[0].strip()
                pt0, pt1, pt2 = line1.split('-')[0], line1.split('-')[1], line1.split('-')[2]
                geneSymbolExp = pt0 + '-' + pt1 + '-' + pt2
                #print(geneSymbolExp)

                if geneSymbolExp in dict01:
                    line1 = line1 + "," + dict01[geneSymbolExp]
                    print("line: ", line1)
                fw.writelines(line1 + "\n")