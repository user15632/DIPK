import numpy as np
import pandas as pd
import joblib

GEO02_nCR_dict = dict()
GEO02_pCR_dict = dict()
dataset = pd.read_csv('raw.RPKM.csv', header=None, sep=',', low_memory=False)
Cell = [str(_) for _ in list(dataset.iloc[0, 1:])]
Data = np.array(dataset.iloc[1:, 1:], dtype=np.float32)

dataset = pd.read_csv('GSE32646.csv', header=None, sep='\t', low_memory=False)
# Cell_ = [str(_) for _ in list(dataset.iloc[:, 0])]  # Cell == Cell_
Label_ = [str(_).split(':')[1][1:] for _ in list(dataset.iloc[:, 1])]

for i in range(len(Label_)):
    if Label_[i] == 'nCR':
        GEO02_nCR_dict[Cell[i]] = Data[:, i].tolist()
    elif Label_[i] == 'pCR':
        GEO02_pCR_dict[Cell[i]] = Data[:, i].tolist()
joblib.dump(GEO02_nCR_dict, 'GEO02_nCR_dict.pkl')
joblib.dump(GEO02_pCR_dict, 'GEO02_pCR_dict.pkl')
