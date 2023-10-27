import joblib
import numpy as np
import pandas as pd

dataset = pd.read_csv('../../Dataset/Cell_Drug_IC50.csv', header=0)
Cell_List = [str(_).split('\t')[0] for _ in list(dataset.iloc[:, 0])]

f = open('../../../Data/Metadata.txt', encoding='gbk')
Cell_List_Remove = []
for each_row in f:
    Cell = each_row.strip().split('\t')[1]
    Cell_List_Remove.append(Cell.split('_')[0])
Cell_List_Remove = Cell_List_Remove[2:]

Cell_Remain = sorted(list(set(Cell_List) - set(Cell_List_Remove)))

dataset = pd.read_csv('../CCLE_RNAseq_rsem_genes_tpm_sel.txt', header=None, sep='\t', low_memory=False)
Cells = list(dataset.iloc[0, 1:])
Features = np.array(dataset.iloc[1:, 1:])

RNAseq_Dict = dict()
for i in range(len(Cells)):
    if Cells[i] in Cell_Remain:
        ft = np.array([float(_) for _ in Features[:, i]])
        ft = np.log2(ft + 1)
        RNAseq_Dict[Cells[i]] = ft.tolist()
joblib.dump(RNAseq_Dict, 'RNAseq_Dict.pkl')
