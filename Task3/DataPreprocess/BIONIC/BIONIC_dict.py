import joblib
import numpy as np
import pandas as pd

f = open('../TPM/gene_list_sel.txt', encoding='gbk')
gene_list = []
for each_row in f:
    gene_list.append(each_row.strip())

BIONIC_dict = dict()
dataset = pd.read_csv('../../../Data/human_ppi_features.tsv', header=0)
data = list(dataset.iloc[:, 0])
for each_row in data:
    row = each_row.split()
    gene = row[0]
    if gene in gene_list:
        ft = np.array([float(_) for _ in row[1:]])
        """mean = np.mean(ft)
        std = np.std(ft)
        ft = (ft - mean) / std"""
        BIONIC_dict[gene_list.index(gene)] = ft.tolist()
print(len(BIONIC_dict))
joblib.dump(BIONIC_dict, 'BIONIC_dict.pkl')
