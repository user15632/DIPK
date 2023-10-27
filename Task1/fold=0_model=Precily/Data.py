from torch.utils.data import Dataset
from abc import ABC
import pandas as pd
import joblib
import torch

from DataConfig import *

SMILESVec_dict = joblib.load('../Dataset/SMILESVec_dict.pkl')
Pathway_dict = joblib.load('../Dataset/Pathway_dict.pkl')

val_set_path = '../Dataset/lenient_split_fold_{}_validation.csv'.format(fold_num)
test_set_path = '../Dataset/lenient_split_test.csv'
total_set_path = '../Dataset/lenient_split_fold_0_dataset.csv'


def GetData(csv_path):
    dataset = pd.read_csv(csv_path, header=0)
    Cell = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug = [str(_) for _ in list(dataset.iloc[:, 1])]
    IC50 = [float(_) for _ in list(dataset.iloc[:, -1])]

    Data = []
    for ii in range(len(Cell)):
        data = Pathway_dict[Cell[ii]] + SMILESVec_dict[Drug[ii]] + [IC50[ii]]
        Data.append(data)

    return torch.tensor(Data, dtype=torch.float32)


def LenientRemove(Cell, Drug, IC50, val_csv_path, test_csv_path):
    dataset = pd.read_csv(val_csv_path, header=0)
    Cell_ = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug_ = [str(_) for _ in list(dataset.iloc[:, 1])]
    dataset = pd.read_csv(test_csv_path, header=0)
    Cell_ += [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug_ += [str(_) for _ in list(dataset.iloc[:, 1])]

    Pair_ = []
    for ii in range(len(Drug_)):
        pair_ = (Cell_[ii], Drug_[ii])
        Pair_.append(pair_)

    CellList = []
    DrugList = []
    IC50List = []
    for ii in range(len(Drug)):
        pair = (Cell[ii], Drug[ii])
        if pair not in Pair_:
            CellList.append(Cell[ii])
            DrugList.append(Drug[ii])
            IC50List.append(IC50[ii])

    return CellList, DrugList, IC50List


def GetTrainData(total_csv_path, val_csv_path, test_csv_path):
    dataset = pd.read_csv(total_csv_path, header=0)
    Cell = [str(_) for _ in list(dataset.iloc[:, 0])]
    Drug = [str(_) for _ in list(dataset.iloc[:, 1])]
    IC50 = [float(_) for _ in list(dataset.iloc[:, -1])]

    Cell, Drug, IC50 = LenientRemove(Cell, Drug, IC50, val_csv_path, test_csv_path)

    Data = []
    for ii in range(len(Cell)):
        data = Pathway_dict[Cell[ii]] + SMILESVec_dict[Drug[ii]] + [IC50[ii]]
        Data.append(data)

    return torch.tensor(Data, dtype=torch.float32)


if debug == 0:
    Gtrain = GetTrainData(total_set_path, val_set_path, test_set_path)
else:
    Gtrain = GetData(val_set_path)
# Gval = GetData(val_set_path)
Gtest = GetData(test_set_path)


class CollateFn:
    def __init__(self, follow_batch=None, exclude_keys=None):
        self.follow_batch = follow_batch
        self.exclude_keys = exclude_keys

    def __call__(self, batch):
        batch_data = torch.stack(batch)
        return batch_data


class MyDataSet(Dataset, ABC):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, idx):
        data = self._data[idx]
        return data

    def __len__(self):
        return len(self._data)
