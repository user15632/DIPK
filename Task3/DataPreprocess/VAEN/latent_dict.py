import numpy as np
import pandas as pd
import joblib


def fun(n1, n2):
    dataset = pd.read_csv('{}.CCLE.latent.tsv'.format(n1), header=0, sep='\t')
    Cell = [str(_).split('_')[0] for _ in dataset.iloc[:, 0]]
    Data = np.array(dataset.iloc[:, 1:], dtype=np.float32)
    latent_dict = dict()
    for i in range(len(Cell)):
        latent_dict[Cell[i]] = Data[i, :].tolist()
    joblib.dump(latent_dict, 'latent_dict_{}.pkl'.format(n2))
    return latent_dict


latent_dict0 = fun(23, 0)
latent_dict1 = fun(24, 1)
latent_dict2 = fun(35, 2)
latent_dict3 = fun(57, 3)
latent_dict4 = fun(83, 4)
