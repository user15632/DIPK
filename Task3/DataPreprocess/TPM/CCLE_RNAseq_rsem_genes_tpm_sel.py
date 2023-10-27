import numpy as np
import joblib

GeneName_GeneID_Dict = joblib.load('GeneName_GeneID_Dict.pkl')
GeneID = []
for each in GeneName_GeneID_Dict:
    GeneID += GeneName_GeneID_Dict[each]

f = open('gene_list_sel.txt', encoding='gbk')
gene_name = []
for each_row in f:
    gene_name.append(each_row.strip())

f = open('../../../Data/CCLE_RNAseq_rsem_genes_tpm_20180929.txt', encoding='gbk')
other_lines = dict()
i = 0
for each_row in f:
    row = each_row.strip().split('\t')
    if i == 0:
        i = 1
        first_line = row[2:]
        line = []
        for each in first_line:
            line.append(each.split('_')[0])
        with open('CCLE_RNAseq_rsem_genes_tpm_sel.txt', 'a') as file0:
            print('\t'.join(['gene_name'] + line), file=file0)
    else:
        id = row[0]
        if id in GeneID:
            other_lines[id] = row[2:]

other_lines_gene = []
for each in gene_name:
    id = GeneName_GeneID_Dict[each]
    if len(id) == 1:
        row = [each] + other_lines[id[0]]
        other_lines_gene.append('\t'.join(row))
    else:
        ft = np.array([0.0] * len(other_lines[id[0]]))
        for i in range(len(id)):
            ft += np.array([float(_) for _ in other_lines[id[i]]])
        ft = ft / len(id)
        row = [each] + [str(_) for _ in ft.tolist()]
        other_lines_gene.append('\t'.join(row))

for each in other_lines_gene:
    with open('CCLE_RNAseq_rsem_genes_tpm_sel.txt', 'a') as file0:
        print(each, file=file0)
