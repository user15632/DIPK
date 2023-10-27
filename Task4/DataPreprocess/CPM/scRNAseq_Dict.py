import joblib
import numpy as np

Cells, genes, ft = joblib.load('GSE157220_CPM_data_pre.pkl')

f = open('../gene_list_sel.txt', encoding='gbk')
gene_list = []
for each_row in f:
    gene_list.append(each_row.strip())

gene_index = []
for each in gene_list:
    if each in genes:
        index = genes.index(each)
    else:
        index = -1
    gene_index.append(index)

n = []
scRNA = []
for i in range(len(Cells)):
    n_ = 0
    feature = []
    for each in gene_index:
        if each >= 0:
            feature.append(ft[each][i])
        else:
            n_ += 1
            feature.append(0.0)
    n.append(n_)
    scRNA.append(feature)

scRNA_dict = dict()
for i in range(len(Cells)):
    f = np.array(scRNA[i], dtype=np.float32)
    scRNA_dict[Cells[i]] = f.tolist()
joblib.dump(scRNA_dict, 'scRNAseq_Dict.pkl')
