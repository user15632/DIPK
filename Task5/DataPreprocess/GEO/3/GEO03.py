import numpy as np
import pandas as pd
import joblib

GEO03_RD_dict = dict()
GEO03_pCR_dict = dict()
dataset = pd.read_csv('raw.RPKM.csv', header=None, sep=',', low_memory=False)
Cell = [str(_) for _ in list(dataset.iloc[0, 1:])]
Data = np.array(dataset.iloc[1:, 1:], dtype=np.float32)

dataset = pd.read_csv('GSE20194.csv', header=None, sep='\t', low_memory=False)
# Cell_ = [str(_) for _ in list(dataset.iloc[:, 0])]  # Cell == Cell_
Label_1 = [str(_).split(':')[1][1:] for _ in list(dataset.iloc[:, 1])]
Label_2 = [str(_).split(':')[1][1:] for _ in list(dataset.iloc[:, 2])]
Label_3 = [str(_).split(':')[1][1:] for _ in list(dataset.iloc[:, 3])]
Label_ = []
for i in range(len(Label_1)):
    if Label_1[i] == 'pCR' or Label_2[i] == 'pCR' or Label_3[i] == 'pCR':
        Label_.append('pCR')
    elif Label_1[i] == 'RD' or Label_2[i] == 'RD' or Label_3[i] == 'RD':
        Label_.append('RD')
    else:
        print(i)

for i in range(len(Label_)):
    if Label_[i] == 'RD':
        GEO03_RD_dict[Cell[i]] = Data[:, i].tolist()
    elif Label_[i] == 'pCR':
        GEO03_pCR_dict[Cell[i]] = Data[:, i].tolist()
joblib.dump(GEO03_RD_dict, 'GEO03_RD_dict.pkl')
joblib.dump(GEO03_pCR_dict, 'GEO03_pCR_dict.pkl')
