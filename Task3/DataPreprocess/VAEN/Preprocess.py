import joblib
import numpy as np
import pandas as pd


def getData(path, latent_dict, name):
    dataset = pd.read_csv(path, header=0)
    Cell = [str(_).split('\t')[0] for _ in list(dataset.iloc[:, 0])]
    Drug = [str(_).split('\t')[1] for _ in list(dataset.iloc[:, 0])]
    IC50 = [float(str(_).split('\t')[2]) for _ in list(dataset.iloc[:, 0])]
    Drug_ls = sorted(list(set(Drug)))
    dataset = dict()
    for each in Drug_ls:
        data = []
        for ii in range(len(Cell)):
            if Drug[ii] == each:
                try:
                    data.append(latent_dict[Cell[ii]] + [IC50[ii]])
                except KeyError:
                    continue
        dataset[each] = np.array(data, dtype=np.float32)
    joblib.dump(dataset, name)
    return dataset


dataset1 = getData('../../Dataset/Train.csv', joblib.load('latent_dict_0.pkl'), 'Train_set_0.pkl')
dataset2 = getData('../../Dataset/Train.csv', joblib.load('latent_dict_1.pkl'), 'Train_set_1.pkl')
dataset3 = getData('../../Dataset/Train.csv', joblib.load('latent_dict_2.pkl'), 'Train_set_2.pkl')
dataset4 = getData('../../Dataset/Train.csv', joblib.load('latent_dict_3.pkl'), 'Train_set_3.pkl')
dataset5 = getData('../../Dataset/Train.csv', joblib.load('latent_dict_4.pkl'), 'Train_set_4.pkl')

dataset6 = getData('../../Dataset/Test.csv', joblib.load('latent_dict_0.pkl'), 'Test_set_0.pkl')
dataset7 = getData('../../Dataset/Test.csv', joblib.load('latent_dict_1.pkl'), 'Test_set_1.pkl')
dataset8 = getData('../../Dataset/Test.csv', joblib.load('latent_dict_2.pkl'), 'Test_set_2.pkl')
dataset9 = getData('../../Dataset/Test.csv', joblib.load('latent_dict_3.pkl'), 'Test_set_3.pkl')
dataset0 = getData('../../Dataset/Test.csv', joblib.load('latent_dict_4.pkl'), 'Test_set_4.pkl')
