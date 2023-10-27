import joblib
import numpy as np
import pandas as pd

train_set = pd.read_csv('../../Dataset/Train.csv', header=0)
Ctrain = [str(_).split('\t')[0] for _ in list(train_set.iloc[:, 0])]
test_set = pd.read_csv('../../Dataset/Test.csv', header=0)
Ctest = [str(_).split('\t')[0] for _ in list(test_set.iloc[:, 0])]
Cell_Remain = sorted(list(set(Ctrain + Ctest)))

dataset = pd.read_csv('CCLE_RNAseq_rsem_genes_tpm_sel.txt', header=None, sep='\t', low_memory=False)
Cells = list(dataset.iloc[0, 1:])
Features = np.array(dataset.iloc[1:, 1:])

RNAseq_Dict = dict()
for i in range(len(Cells)):
    if Cells[i] in Cell_Remain:
        ft = np.array([float(_) for _ in Features[:, i]])
        ft = np.log2(ft + 1)
        RNAseq_Dict[Cells[i]] = ft.tolist()
joblib.dump(RNAseq_Dict, 'RNAseq_Dict.pkl')
