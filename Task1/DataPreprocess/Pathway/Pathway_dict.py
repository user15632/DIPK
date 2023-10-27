import joblib
import pandas as pd
import numpy as np

dataset = pd.read_csv('Pathway.csv', header=None, sep=',', low_memory=False)
Cell = [str(_)[1:] for _ in list(dataset.iloc[0, 1:])]
Pathway = np.array(dataset.iloc[1:, 1:], dtype=np.float32)

Pathway_dict = dict()
for i in range(len(Cell)):
    Pathway_dict[Cell[i]] = Pathway[:, i].tolist()
joblib.dump(Pathway_dict, 'Pathway_dict.pkl')
