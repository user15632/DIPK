import numpy as np
import pandas as pd
import joblib

RMA_dict = dict()
dataset = pd.read_csv('../../../Data/Cell_line_RMA_proc_basalExp.txt', header=None, sep='\t', low_memory=False)
Cell = ['.'.join(str(_).split('.')[1:]) for _ in list(dataset.iloc[0, 2:])]
Gene = [str(_) for _ in list(dataset.iloc[1:, 0])]
gene_list = sorted(list(set(Gene)))
RMA_dict['Gene'] = gene_list
Gene_index = [Gene.index(_) for _ in gene_list]

dataset = pd.read_csv('../../../Data/Cell_line_RMA_proc_basalExp.txt', header=0, sep='\t')
RMA = np.array(dataset.iloc[:, 2:])
RMA = RMA[Gene_index, :]
# RMA = (RMA - np.expand_dims(np.mean(RMA, 1), 1)) / np.expand_dims(np.std(RMA, 1), 1)

for i in range(len(Cell)):
    if Cell[i] not in RMA_dict:
        RMA_dict[Cell[i]] = RMA[:, i].tolist()
# joblib.dump(RMA_dict, 'RMA_N_dict.py')

dataframe = pd.DataFrame(RMA_dict)
dataframe.to_csv('RMA_N_dict.csv', index=False, sep=',')
